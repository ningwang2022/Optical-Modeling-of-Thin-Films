# Optical-Modeling-of-Thin-Films :
## References Information
This model is based on the Optical Transfer Matrix model, which can be found in the following paper:

> L. A. A. Pettersson *et al.*, “Modeling photocurrent action spectra of photovoltaic devices based on organic thin films
”, *J. Appl. Phys.* **86**, 487-496 (1999) [[link to the paper]](http://aip.scitation.org/doi/10.1063/1.370757)

And this project is based on the following work：

> C. Marcus Chuang, "Optical-Modeling", (2015) [[Source code: https://github.com/marcus-cmc/Optical-Modeling]](https://github.com/marcus-cmc/Optical-Modeling)

where we contributed to updating some of the functions used in the **latest packages** and modifying some of the code, in order to make the model receive our **experimental data** and save the figures.

## Experimental Data

We measured the optical parameters of a series of prepared film samples using ellipsometry. So we obtained the key optical parameters **n** and **k**. For example, the figure below shows the results for sample (PM6L8BO):

<img src="/Fig/Complex refractive index of PM6L8B0.png" width="600" >

## Examples

After we determine the optical parameters and thickness of each layer, we start our simulation by running `RunModeling.py`. Also, there are the setup information for each layer (metal electrodes are ignored for now)

```python
Device = [
          ("Glass"  , 30), # nm
          ("ITO"    , 30), 
          ("PEDOT:PSS"    , 30),
          ("PM6L8BO"    , 120),
          ("PDINN"     , 30)
         ]
```
<img src="/Fig/Absorption.png" width="600" >

<img src="/Fig/Efield.png" width="600" >
## Requirements
Actually, our work uses only the light absorption and light field distribution simulation parts. Our project will work fine in python 3.9 with the following dependencies:

| Package     | Version   |
|-------------|-----------|
| NumPy       | 1.24.3    |
| Matplotlib  | 3.7.1     |
| Pandas      | 2.0.1     |



