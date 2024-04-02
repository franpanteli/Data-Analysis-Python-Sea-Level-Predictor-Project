# Python-Data-Analysis-Sea-Level-Predictor-Project
### About This Repository
I independently completed freeCodeCamp's [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python#data-analysis-with-python-course) certification, to invest in my data analytics skills with Python. This repository contains my independent problem-solving work as part of the [fifth project](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor) in this curriculum. I devised a Python script for this, which used linear regression with SciPy to produce two predictions of global sea level rise by 2050.

### Workflow
Notes on the task brief for this project were first written, which are [here](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/1%20project-task-notes.txt). The project boilerplate files were next cloned in a Gitpod environment. This included CSV time series data for the global average sea level ([epa-sea-level.csv](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/epa-sea-level.csv)). Python was desired which produced a time series plot for this data, for the global sea level from 1880-2014. Two linear regression lines were desired for this, both of which were extrapolated to the year 2050 to predict the sea level rise by then. The gradient of these regression lines equated to the rate of sea level rise per year. 

This plot was to be produced from data provided in a CSV dataset ([epa-sea-level.csv](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/epa-sea-level.csv)) by a plotting function to be written in Python. The first linear regression line on this plot was to be based on data from the entire dataset (from 1880-2014) and the second was to be based on data from 2000-2014. This plotting function produced two estimates for global sea level rise by the year 2050, with the prior being a less dire estimation of this. 

The plotting function which produced this desired time series was written with Python in the project [sea_level_predictor.py](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/sea_level_predictor.py) file. This was annotated with problem solving approaches required to generate this plot from the data. For this, CSV data and modules were first imported. The time series plot was then generated from this, with two linear regression lines. Axes were added to this plot and it was saved by the function as [sea_level_plot.png](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/sea_level_plot.png), provided below. 

<img width="533" alt="Screenshot 2024-04-02 at 15 30 57" src="https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/assets/131474705/6ea2168c-aa73-4b92-bb4f-ba4d987c3c74">

Project files were pushed to this repository once all unit tests ([test_module.py](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/test_module.py) and [main.py](https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project/blob/main/main.py)) had successfully passed and its URL was submitted. This aided in developing statistical and data analytics skills with Numpy and marked the completion of the fifth and final project in the course. 

### To Clone This Repository
```
git clone https://github.com/franpanteli/Data-Analysis-Python-Sea-Level-Predictor-Project.git
```
