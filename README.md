<h1 align = "center">
	<img height = "175" width = "275" src = "./assets/logo.png"> <br>
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
