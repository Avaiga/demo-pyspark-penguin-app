# Demo Pytorch Penguin App

## Usage
- [Usage](#usage)
- [Demo Pytorch Penguin App](#what-is-demo-pytorch-penguin-app)
- [Directory Structure](#directory-structure)
- [License](#license)
- [Installation](#installation)
- [Contributing](#contributing)
- [Code of conduct](#code-of-conduct)

## What is Demo Pytorch Penguin App

Taipy is a Python library for creating Business Applications. More information on our
[website](https://www.taipy.io).

[Demo Pytorch Penguin App](https://github.com/Avaiga/demo-pytorch-penguin-app) 
focuses on the seamless integration of Pytorch (a distributed computing framwork - enabling large scale data processing) with Taipy, a Python library used for pipeline orchestration and scenario management.

### Demo Type
- **Level**: Intermediate
- **Topic**: GUI/Core

## How to run

This demo works with a Python version superior to 3.8. Install the dependencies of the *requirements.txt* and run the *main.py*.

## Introduction
We'll design a workflow which performs two main tasks:
1- Spark task (spark_process):
- Load the data;
- Group the data by "species", "island" and "sex";
- Find the mean of the other columns ("bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g");
- Save the data.

2- Python task (filter):
- Load the output data saved previously by the Spark task;
- Given a "species", "island" and "sex", return the aggregated values.

## Directory Structure

- `src/`: Contains the demo source code.
    - `data/`
        ├─ `penguin.csv`: a sample dataset.
    - `penguin_spark_app.py`: Script running our spark instance.
    - `config.py`: Taipy configuration which models our data workflow.
    - `main.py`: Script creating application.
- `CODE_OF_CONDUCT.md`: Code of conduct for members and contributors of _demo-dask-customer-analysis_.
- `CONTRIBUTING.md`: Instructions to contribute to _demo-dask-customer-analysis_.
- `INSTALLATION.md`: Instructions to install _demo-dask-customer-analysis_.
- `LICENSE`: The Apache 2.0 License.
- `README.md`: Current file.

## License
Copyright 2022 Avaiga Private Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at
[http://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

## Installation

Want to install _Demo Dask Customer Analysis_? Check out our [`INSTALLATION.md`](INSTALLATION.md) file.

## Contributing

Want to help build _Demo Dask Customer Analysis_? Check out our [`CONTRIBUTING.md`](CONTRIBUTING.md) file.

## Code of conduct

Want to be part of the _Demo Dask Customer Analysis_ community? Check out our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) file.
