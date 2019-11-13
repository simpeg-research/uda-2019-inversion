# uda-2019-inversion

[![Build Status](https://travis-ci.com/simpeg-research/uda-2019-inversion.svg?branch=master)](https://travis-ci.com/simpeg-research/uda-2019-inversion)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simpeg-research/uda-2019-inversion/master?filepath=gravity-inversion.ipynb)
[![License](https://img.shields.io/github/license/simpeg-research/uda-2019-inversion.svg)](https://github.com/simpeg-research/uda-2019-inversion/blob/master/LICENSE)
[![SimPEG](https://img.shields.io/badge/powered%20by-SimPEG-blue.svg)](http://simpeg.xyz)


## Summary

This notebook illustrates the SimPEG code used to invert Bouguer gravity data collected at Laguna del Maule volcanic field, Chile. Refer to [Miller et al 2017 EPSL](https://doi.org/10.1016/j.epsl.2016.11.007) for full details.

Originally implemented in the [SimPEG Examples](http://docs.simpeg.xyz/content/examples/04-grav/plot_laguna_del_maule_inversion.html#sphx-glr-content-examples-04-grav-plot-laguna-del-maule-inversion-py)


## Contents

There is one notebooks in this repository:

- [gravity-inversion.ipynb](gravity-inversion.ipynb)

## Usage

### online
You can run these notebooks online through mybinder by clicking on the badge below:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simpeg-research/uda-2019-inversion/master?filepath=gravity-inversion.ipynb)

### locally
To run the notebooks locally, you will need to have python installed,
preferably through [anaconda](https://www.anaconda.com/download/). Please download 
Python 3.7 or greater. 

Once you have downloaded and installed anaconda, you can then clone this repository. 
From a command line (if you are on windows, please use the anaconda terminal that came with the installation)
run

```
git clone https://github.com/simpeg-research/uda-2019-inversion.git
```

Then `cd` into the `uda-2019-inversion` directory:

```
cd uda-2019-inversion
```

To setup your software environment, we recommend you use the provided conda environment

```
conda env create -f environment.yml
conda activate uda-2019-inversion
```

You can then launch Jupyter

```
jupyter notebook
```

Jupyter will then launch in your web-browser.

## Running the notebooks

Each cell of code can be run with `shift + enter` or you can run the entire notebook by selecting `cell`, `Run All` in the toolbar.

<img src="https://em.geosci.xyz/_images/run_all_cells.png" width=80% align="middle">

For more information on running Jupyter notebooks, see the [Jupyter Documentation](https://jupyter.readthedocs.io/en/latest/)

If you are new to Python, I highly recommend taking a look at:
- [A Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
- [The Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

## Issues

Please [make an issue](https://github.com/simpeg-research/uda-2019-inversion/issues) if you encounter any problems while trying to run the notebooks.

## Citation

If you build upon or use these examples in your work, please cite:

Miller, Craig A., et al. "3D gravity inversion and thermodynamic modelling reveal properties of shallow silicic magma reservoir beneath Laguna del Maule, Chile." Earth and Planetary Science Letters 459 (2017): 14-27.

```
@article{miller20173d,
  title={3D gravity inversion and thermodynamic modelling reveal properties of shallow silicic magma reservoir beneath Laguna del Maule, Chile},
  author={Miller, Craig A and Williams-Jones, Glyn and Fournier, Dominique and Witter, Jeff},
  journal={Earth and Planetary Science Letters},
  volume={459},
  pages={14--27},
  year={2017},
  publisher={Elsevier}
}
```