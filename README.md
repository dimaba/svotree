# svotree

## Implemented measures of Social Value Orientation in oTree

This repository contains templates and functions which implement common measures of Social Value Orientation in oTree.
The two measures currently implemented are the Nine-Item Triple Dominance measure (Van Lange, Otten & Joireman, 1997) and the Slider Measure (Murphy, Ackermann & Handgraaf, 2011). 
For the Slider Measure, a variant with continuous choices and one with discrete choices are included.

This repository contains Django/HTML templates with associated JavaScript functionality to display these SVO measures
to participants, as well as Python functions to evaluate the resulting input.
 
## Installation and usage instructions
Out of the box, this repository functions as an oTree app which can be placed in your oTree folder and included in the 
app sequence for your session. Within the app you can of course freely choose which measures (pages) are displayed. You 
can also modify any aspect of the styling or functionality. 

#### Recommended
- Clone or download the full contents of this repository directly from this page. 
- Place the `svoTree` folder in your oTree experiment directory 
- Add `svoTree` to the app sequence of any sessions in which you want to use it
This is the recommended installation method. 

## Examples
To try all measures of SVO included in `svoTree`, add `svoTree` to the app sequence of an existing
session config or create a new session config which has `svoTree` in the app sequence. To make sure you see all included
measures when running this session, check that all included pages are listed in the page sequence at the bottom of 
`views.py`.

The `views.py` contains complete working examples of pages which display, collect input from, and calculate Social Value
Orientation for each of the included measures. 

## Contents

Included in `svoTree` are several measures of Social Value Orientation. So far, the repository contains two measures. First,
the measure which is historically most commonly used: the Nine-Item Triple Dominance Measure (see Au & Kwong, 2004). Second,
a more recently introduced measure which has been gaining popularity and offers a more fine-grained assessment of Social Value
Orientation: the Slider Measure (Murphy, Ackermann & Handgraaf, 2011). For each of these measure, `svoTree` includes 
templates (with associated JavaScript files) to display these measures, as well as functions to assess the resulting input.
In `views.py` you will find a view for each included measure, which can be used directly or can be taken as an example which
shows what you will need to implement in your own views in order to use `svotree`'s functions and templates. 

### Nine-Item Triple Dominance measure

### Slider Measure

#### Continuous variant

#### Discrete variant


## References
1. Au, W. T., & Kwong, J. Y. Y. (2004). Measurements and effects of social-value orientation in social dilemmas. In R. Suleiman, D. V Budescu, I. Fischer, & D. M. Messick (Eds.), Contemporary psychological research on social dilemmas (pp. 71–98). Cambridge: Cambridge University Press.
2. Murphy, R. O., Ackermann, K. A., & Handgraaf, M. J. J. (2011). Measuring Social Value Orientation. Judgment and Decision Making, 6(8), 1–12. http://doi.org/10.2139/ssrn.1804189
3. Van Lange, P. a. M., Otten, W., De Bruin, E. M. N., & Joireman, J. a. (1997). Development of prosocial, individualistic, and competitive orientations: Theory and preliminary evidence. Journal of Personality and Social Psychology, 73(4), 733–746. doi:10.1037//0022-3514.73.4.733

## License

[MIT License](LICENSE)