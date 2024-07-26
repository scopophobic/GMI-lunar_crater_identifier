# Lunar Crater Analysis and Information System

## Overview

This project aims to create an advanced image search engine for lunar craters, leveraging data from multiple lunar missions (TMC, IIRS, OHRC, DFSAR). By integrating high-resolution topographic data, mineral composition maps, precise morphological images, and sub-surface feature analysis, we offer a comprehensive solution for identifying and analyzing lunar craters. Additionally, our system uses advanced LLMs to provide detailed information about each crater, including surrounding area details, morphological features, and facts sourced from the internet.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Data Sources](#data-sources)
5. [Models Used](#models-used)
6. [Contributing](#contributing)
7. [Acknowledgements](#acknowledgements)
8. [License](#license)

## Introduction

### Problem Statement

The identification and detailed analysis of lunar craters are crucial for understanding the moon's geological history. Traditional methods require extensive manual effort and analysis. This project automates crater identification and provides comprehensive information using multiple data sources and advanced machine learning models.

### Objectives

- Automate the detection of lunar craters using high-resolution data.
- Provide detailed information about each crater, including topography, mineral composition, and morphological features.
- Integrate multiple datasets to enhance the accuracy and comprehensiveness of the analysis.

## Features

- **Automated Crater Detection**: Use CNNs to detect craters in lunar images.
- **Comprehensive Analysis**: Extract and provide details such as depth, diameter, volume, thermal properties, and sub-surface features.
- **LLM Integration**: Utilize an open-source LLM to generate detailed textual descriptions of the craters.
- **Interactive Visualization**: Annotated images and interactive maps displaying detected craters and their coordinates.

## Architecture

![Architecture Diagram](projectinfo/readme/architecture-diagram.png)


## Data Sources
- TMC: Topographic data including crater depth, diameter, and volume.
- IIRS: Mineral composition and thermal properties.
- OHRC: High-resolution morphological features.
- DFSAR: Sub-surface features such as dielectric properties and surface roughness.

## Models Used
- Convolutional Neural Networks (CNNs): For feature extraction from each data source.
- Region Proposal Networks (RPNs): For proposing regions of interest.
- Box Regression and Classification: For detecting and classifying craters.
- LLM (e.g., LLMA/mistral): For generating detailed textual descriptions of craters.

## Contributing
We welcome contributions from the community. Please read our [contributing guidelines]() for more details.


## Acknowledgements
- ISRO for providing the datasets. [link](https://chmapbrowse.issdc.gov.in/MapBrowse/)
- TensorFlow and PyTorch for their open-source machine learning libraries.
- Hugging Face for their open-source LLM implementations.


## License
This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.



