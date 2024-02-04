# Credit Assignment OpenScope Project Deployment Scripts

This repository contains the stimulus scripts used to generate the stimuli for the **Credit Assignment project**, an [Allen Institute for Brain Science](https://alleninstitute.org/what-we-do/brain-science/) [OpenScope](https://alleninstitute.org/division/mindscope/openscope/) project. 
&nbsp;

The Credit Assignment experiment was conceptualized by [Joel Zylberberg](http://www.jzlab.org/) (York University), [Blake Richards](http://linclab.org/) (McGill University), [Timothy Lillicrap](http://contrastiveconvergence.net/~timothylillicrap/index.php) (DeepMind) and [Yoshua Bengio](https://yoshuabengio.org/) (Mila), and the stimuli were coded by [Colleen Gillon](https://colleenjg.github.io/).

These scripts **have been updated** since the dataset described in [Gillon _et al._, 2023, _Sci Data_](https://doi.org/10.1038/s41597-023-02214-y) was collected. For the exact scripts used in the experiments reported in that paper, see the [commit tagged as `production_v1`](https://github.com/colleenjg/cred_assign_stimuli_deployed/tree/production_v1). 
&nbsp;

**NOTE:** Whereas _this_ repository contains the **exact scripts** deployed for data collection in the OpenScope pipeline, the [`cred_assign_stimuli`](https://github.com/colleenjg/cred_assign_stimuli) repository contains the same base code, but modified to allow users to conveniently visualize, reproduce and save the stimuli described in our dataset descriptor paper, [Gillon _et al._, 2023, _Sci Data_](https://doi.org/10.1038/s41597-023-02214-y), and analysis paper, [Gillon, Pina _et al._, 2024, _J Neurosci_](https://www.jneurosci.org/content/44/5/e1009232023). It also contains a more detailed description of the stimulus design.  

## Stimulus design
Sparse Gabor sequences (adapted from [Homann _et al._, 2022, _PNAS_](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8812573/))
&nbsp;

## Installation
### Dependencies:
- Windows OS (see **Camstim package**)
- python 2.7
- psychopy 1.82.01
- camstim 0.2.4
&nbsp;

### Camstim 0.2.4: 
- Built and licensed by the [Allen Institute](https://alleninstitute.org/).
- Written in **Python 2** and designed for **Windows OS** (requires `pywin32`).
- Pickled stimulus presentation logs are typically saved under `user/camstim/output`.
&nbsp;

### Installation with [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html):
1. Navigate to repository and install conda environment.  
    `conda env create -f cred_assign_stimuli.yml`
2. Activate the environment.  
    `conda activate cred_assign_stimuli`
3. Install the Allen Institute's `camstim` package in the environment.  
    `pip install camstim/.`
4. Download and install [`AVbin`](https://avbin.github.io/AVbin/Download.html) for your OS.  
&nbsp;

## Scripts  
### `pilot_scripts` : scripts used for the pilot deployment
- `habituation_rig` : scripts used on the habituation rig. For each habituation day, a different script is used, shared across all subjects,  
e.g., run `python pilot_scripts/habituation_rig/day7.py`.  
- `ophys_rig` : scripts used on the optical physiology rig. For each experiment day, a different script is used, shared across all subjects,  
e.g., run `python pilot_scripts/ophys_rig/ophys_record.py`.  
&nbsp;

### `production_scripts` : scripts used for the production deployment
_Not yet created._
&nbsp;

## Log files
- Pickled stimulus presentation logs are typically saved under `user/camstim/output`.
- Sweep parameters are under a few keys of `['stimuli'][n]`, where `n` is the stimulus number.
- Stimulus parameters are in dictionaries stored under: `['stimuli'][n]['stim_params']`.  
&nbsp;

## Reproduction
- There are several randomly generated components to the stimuli in each session:  
> 1) Gabor positions and sizes,  
> 2) Gabor sequence block order, 
> 3) Gabor sequence orientations,  
> 4) Unexpected event ("surprise") onsets and duration.
- The stimuli can be reproduced using the **recorded seed**, as the random state is used to generate all 4 random components.
- The same display size must be reused during reproduction.

## Code
Code and documentation (excluding `camstim`) built by Colleen Gillon (colleen _dot_ gillon _at_ mail _dot_ utoronto _dot_ ca).

## Citations

To cite the **dataset** paper:
```
@Article{GillonLecoq2023,
  title={Responses of pyramidal cell somata and apical dendrites in mouse visual cortex over multiple days},
  author={Gillon, Colleen J. and Lecoq, J{\'e}r{\^o}me A. and Pina, Jason E. and Ahmed, Ruweida and Billeh, Yazan and Caldejon, Shiella and Groblewski, Peter and Henley, Timothy M. and Kato, India and Lee, Eric and Luviano, Jennifer and Mace, Kyla and Nayan, Chelsea and Nguyen, Thuyanh and North, Kat and Perkins, Jed and Seid, Sam and Valley, Matthew T. and Williford, Ali and Bengio, Yoshua and Lillicrap, Timothy P. and Zylberberg, Joel and Richards, Blake A.},
  journal={Scientific Data},
  year={2023},
  date={May 2023},
  publisher={Cold Spring Harbor Laboratory},
  volume={10},
  number={1},
  pages={287},
  issn={2052-4463},
  doi={10.1038/s41597-023-02214-y},
  url={https://www.nature.com/articles/s41597-023-02214-y},
}
```

To cite the **analysis** paper:
```
@Article{GillonPina2024,
  title={Responses to pattern-violating visual stimuli evolve differently over days in somata and distal apical dendrites},
  author={Gillon, Colleen J. and Pina, Jason E. and Lecoq, J{\'e}r{\^o}me A. and Ahmed, Ruweida and Billeh, Yazan and Caldejon, Shiella and Groblewski, Peter and Henley, Timothy M. and Kato, India and Lee, Eric and Luviano, Jennifer and Mace, Kyla and Nayan, Chelsea and Nguyen, Thuyanh and North, Kat and Perkins, Jed and Seid, Sam and Valley, Matthew T. and Williford, Ali and Bengio, Yoshua and Lillicrap, Timothy P. and Richards, Blake A. and Zylberberg, Joel},
  journal={Journal of Neuroscience},
  year = {2024},
  date = {Jan 2024},
  publisher = {Society for Neuroscience},
  volume = {44},
  number = {5},
  pages = {1-22},
  issn = {0270-6474},
  doi = {10.1523/JNEUROSCI.1009-23.2023},
  url = {https://www.jneurosci.org/content/44/5/e1009232023},
}
```