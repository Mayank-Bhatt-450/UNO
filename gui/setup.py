import cx_Freeze
executables=[cx_Freeze.Executable("test.py")]
cx_Freeze.setup(
name='guno_lol',
options={"build_exe":{
                        "packages":["pygame","random","time","threading",
                                    "json","requests","webbrowser"],
                        "include_files":["process.png"]
                    }
        },
executables=executables
)
