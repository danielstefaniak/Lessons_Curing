import matplotlib.pylab as plt
import seaborn as sns

#### Plot layout
sns.set_style("ticks")
sns.set_context("notebook", font_scale=1)
sns.set_palette("tab10")
plt.rcParams["figure.dpi"] = 100
plt.rcParams["figure.figsize"] = (9, 4.5)
plt.rcParams['text.usetex'] = False

#### Axis labels
labels = dict(doc=r"Degree of Cure $X \; [-]$",
             Tg=r"Glass Transition Temperature $T_g \; [^\circ C]$",
             temp=r"Temperature $\vartheta \; [^\circ C]$",
             X_max=r"Max. Degree of Cure $X_{\max} \; [-]$",
             time=r"Time $t \; [min]$")