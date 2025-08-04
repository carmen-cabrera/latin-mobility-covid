# Latin America mobility during COVID-19

This repository contains the code developed for the study:\
**"Sustained changes to urban mobility after COVID-19 amplified socio-economic inequalities in Latin America."**

The analysis draws on anonymised, aggregated Meta-Facebook mobility data from Argentina, Chile, and Colombia (March 2020–May 2022), examining long-term changes in mobility across socio-economic and rural–urban gradients.

Due to data licensing restrictions, the dataset is not included. However, code and instructions are provided for reproducing the analysis with approved access.



## System Requirements

-   Python version: 3.10.9
-   Operating system: macOS, Linux, or Windows
-   Hardware: no non-standard hardware required; tested on a typical desktop/laptop machine.

All dependencies are managed through Conda (see `environment.yml`).



## Installation Guide

### 1. Clone the repository

```{bash}
git clone https://github.com/ycarmen-cabrera/latin-mobility-covid.git 
cd latin-mobility-covid
```

### 2. Create and activate the environment

```{bash}
conda env create -f environment.yml conda activate geo-env
```

### 3. Launch Jupyter Notebooks

```{r}
jupyter notebook
```



## Demo Instructions

No demo dataset is included in this repository due to restrictions on the original data.

If you have access to the Meta-Facebook Data for Good datasets, place the relevant files into a /data folder and update paths in the notebooks accordingly.

**Expected output**

The code will generate:

-   Decomposed mobility trends
-   Recovery metrics and imputed time series
-   Visualisations for different spatial and socioeconomic strata

Each notebook can be run on a standard desktop machine with 16 GB RAM.



## Reproducing the analysis

To reproduce the analysis:

-   Place your mobility and population data into a /data directory
-   Follow the notebook sequence
-   Modify file paths as needed in the notebooks



## License

This code is released under the [MIT License](LICENSE).



## Contact

Carmen Cabrera
University of Liverpool
email: c.cabrera@liverpool.ac.uk
