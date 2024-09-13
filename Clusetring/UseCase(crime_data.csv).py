# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 09:36:18 2024

@author: Lenovo
"""

'''
Perform clustering for the crime data and identify
the number of clusters formed and draw interference
refer to crime_data.csv dataset.
1. Business Problem 
1.1 Business Objective?
Clustering is a powerful technique in data analysis that helps in grouping similar data points together. For a dataset like "crime_data.csv," the business objectives for clustering could include:

1. **Identifying Crime Hotspots**:
   - **Objective**: Group geographical locations with similar crime patterns.
   - **Outcome**: Law enforcement agencies can allocate resources more effectively, targeting areas with higher crime rates or specific types of crime.

2. **Crime Pattern Analysis**:
   - **Objective**: Detect patterns or trends in crimes, such as identifying areas prone to certain types of crime (e.g., theft, assault).
   - **Outcome**: Develop strategies for crime prevention and community safety initiatives tailored to specific crime types.

3. **Resource Allocation**:
   - **Objective**: Optimize the allocation of police forces and resources by understanding which areas or times have higher crime density.
   - **Outcome**: Better distribution of resources, potentially leading to reduced crime rates and increased public safety.

4. **Community Risk Profiling**:
   - **Objective**: Profile different communities based on crime data to understand which are at higher risk.
   - **Outcome**: Implement targeted awareness and prevention programs in high-risk communities.

5. **Policy Making and Urban Planning**:
   - **Objective**: Provide insights to policymakers for developing urban areas, with considerations for reducing crime.
   - **Outcome**: Inform decisions on where to build infrastructure, improve lighting, or increase police presence.

6. **Predictive Policing**:
   - **Objective**: Use historical crime data to predict future crime clusters and trends.
   - **Outcome**: Proactively prevent crimes by increasing police presence in predicted areas or during predicted times.

Would you like to explore the dataset further, or run some clustering analyses to see how these objectives could be addressed?
 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

