<h1 align = "center">
	effectR <br>
	<a href = "https://www.linkedin.com/in/dpramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/linkedin.svg"/></a>
	<a href = "https://github.com/ZenithClown"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/github.svg"/></a>
	<a href = "https://gitlab.com/ZenithClown/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/gitlab.svg"/></a>
	<a href = "https://www.researchgate.net/profile/Debmalya_Pramanik2"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/researchgate.svg"/></a>
	<a href = "https://www.kaggle.com/dPramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/kaggle.svg"/></a>
	<a href = "https://app.pluralsight.com/profile/Debmalya-Pramanik/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/pluralsight.svg"/></a>
	<a href = "https://stackoverflow.com/users/6623589/"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/stackoverflow.svg"/></a>
    <a href = "https://www.hackerrank.com/dPramanik"><img height="16" width="16" src="https://unpkg.com/simple-icons@v3/icons/hackerrank.svg"/></a>
    <br>
    <a href="https://github.com/ZenithClown/effectR/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ZenithClown/effectR?style=plastic"></a>
    <a href="https://github.com/ZenithClown/effectR/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ZenithClown/effectR?style=plastic"></a>
</h1>

<p align = "justify"><b>effectR</b> a simple implementation to run <i>R</i> codes from <i>python</i>. Module is implemented using <code>subprocess</code>. For simple execution, <a href = "https://stackoverflow.com/a/38096853">follow this link</a>.</p>

```python
import effectR
stdin, stdout, stderr = effectR.ExecuteR(script = '/full/path/script.R')
stdin, stdout, stderr = effectR.ExecuteR(script = '/full/path/script.R', rbin = '/home/username/anaconda3/envs/R/bin/Rscript')
```

<p align = "justify">If R is not installed in the default directory, then pass the <code>rbin</code> arguments. For instance, if R is installed via a <i>anaconda environment</i> then the path will be something like the one specified above.</p>
<p align = "justify">You can add the <i>anaconda-path</i> to <code>~/.bashrc</code> so that R is available system wide.</p>
