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
</h1>

<p align = "justify"><b>effectR</b> a simple implementation to run <i>R</i> codes from <i>python</i>. Module is implemented using <code>subprocess</code>. For simple execution, <a href = "https://stackoverflow.com/a/38096853">follow this link</a>.</p>

```python
import effectR
p = effectR.ExecuteR(script = '/full/path/script.R')
p = effectR.ExecuteR(script = '/full/path/script.R', rbin = '/home/username/anaconda3/envs/R/bin/Rscript')
```

<p align = "justify">If R is not installed in the default directory, then pass the `rbin` arguments. For instance, if R is installed via a <i>anaconda environment</i> then the path will be something like the one specified above.</p>
<p align = "justify">You can add the <i>anaconda-path</i> to <code>~/.bashrc</code> so that R is available system wide.</p>
