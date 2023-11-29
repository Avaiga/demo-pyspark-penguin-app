### app/config.py
import datetime as dt
import os
import subprocess
import sys
from pathlib import Path

import pandas as pd
import taipy as tp
from taipy import Config

SCRIPT_DIR = Path(__file__).parent
SPARK_APP_PATH = SCRIPT_DIR / "penguin_spark_app.py"


input_csv_path = str(SCRIPT_DIR / "penguins.csv")

# -------------------- Data Nodes --------------------

input_csv_path_cfg = Config.configure_data_node(id="input_csv_path", default_data=input_csv_path)
# Path to save the csv output of the spark app
output_csv_path_cfg = Config.configure_data_node(id="output_csv_path")

processed_penguin_df_cfg = Config.configure_parquet_data_node(
    id="processed_penguin_df", validity_period=dt.timedelta(days=1)
)

species_cfg = Config.configure_data_node(id="species")  # "Adelie", "Chinstrap", "Gentoo"
island_cfg = Config.configure_data_node(id="island")  # "Biscoe", "Dream", "Torgersen"
sex_cfg = Config.configure_data_node(id="sex")  # "male", "female"

output_cfg = Config.configure_json_data_node(
    id="output",
)

# -------------------- Tasks --------------------


def spark_process(input_csv_path: str, output_csv_path: str) -> pd.DataFrame:
    proc = subprocess.Popen(
        [
            str(Path(sys.executable).with_name("spark-submit")),
            str(SPARK_APP_PATH),
            "--input-csv-path",
            input_csv_path,
            "--output-csv-path",
            output_csv_path,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()

    if proc.returncode != os.EX_OK:
        raise Exception("Spark training failed")

    df = pd.read_csv(output_csv_path)

    return df


def filter(penguin_df: pd.DataFrame, species: str, island: str, sex: str) -> dict:
    df = penguin_df[(penguin_df.species == species) & (penguin_df.island == island) & (penguin_df.sex == sex)]
    output = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]].to_dict(orient="records")
    return output[0] if output else dict()


spark_process_task_cfg = Config.configure_task(
    id="spark_process",
    function=spark_process,
    skippable=True,
    input=[input_csv_path_cfg, output_csv_path_cfg],
    output=processed_penguin_df_cfg,
)

filter_task_cfg = Config.configure_task(
    id="filter",
    function=filter,
    skippable=True,
    input=[processed_penguin_df_cfg, species_cfg, island_cfg, sex_cfg],
    output=output_cfg,
)

scenario_cfg = Config.configure_scenario(
    id="scenario", task_configs=[spark_process_task_cfg, filter_task_cfg]
)
