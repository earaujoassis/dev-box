# Dev Box

> A Vagrant + Docker + CLI setup for a development box

Ever wanted to have just one Vagrant machine to work across multiple projects? Well, now you can!

## Usage

`git clone` this repository to `$HOME/somewhere` in order to create the path as following: `$HOME/somewhere/dev-box`.
Put the `dev-box/cli/dev-box.py` into your `$PATH`. You may export it (eg. `export PATH=$PATH:$HOME/somewhere/dev-box/cli`)
or create an alias (eg. `alias dev-box=$HOME/somewhere/dev-box/cli/dev-box.py`). If you don't know the difference or can't
imagine how to proceed with these instructions, please Google it :) From now on I'm assuming you created an alias or
created a symbolic link to `dev-box.py` and named it `dev-box`.

Then, setup the Vagrant machine. It will take a time, but it shouldn't take a lot.

```sh
$ dev-box setup
```

If everything went well (and if it didn't, please post a bug &#x1f41e; in [issues](//github.com/earaujoassis/dev-box/issues)),
you should be able to hook any directory to the Vagrant machine through the command below:

```sh
$ dev-box hook .
```

In this case, `.` is the current working directory (CWD) (`echo $PWD`); it's the current directory where the `dev-box`
command was called. It will basically create a link between the current directory with the Vagrant's VM `/hook` folder.
Thus, you will be able to run any command from within the Vagrant machine using the files and folders listed in `.`.
It is only possible to hook one folder at a time. The CWD will be available in Vagrant's VM `/hook`. You may hook
absolute or relative paths as well. Once the hook is done, you may run commands from within the `/hook` folder:

```sh
$ dev-box console
```
or

```sh
$ dev-box run [commands]
```

The former command opens a /bin/bash shell prompt at Vagrant's VM `/hook`; the latter runs the [commands] as it would be
written directly in the shell, from `$HOME` (arguments and options are proxied to the machine through the `vagrant
ssh -c` command).

To release a hook, just run:

```sh
$ dev-box unhook
```

It is also important to note that docker is available by default &mdahs; you don't have to hook any folder in order to
run a container &mdash; if the image is available. If you run `$ dev-box run docker [commands]` you can build
images or create containers as it would be available in the same machine (well, likely, the only difference is the use
of an IP address different to `127.0.0.1|0.0.0.0|localhost` in this case defaulted to 192.168.44.88 &mdash; you may
change that in `dev-box/Vagrantfile` or creating a `dev-box/Vagrantfile.local` configuring any additional option to the
Vagrant machine).

## Well, what about `docker-machine`?

Yes, I know, `docker-machine` provides (almost) the same services and it also has a larger community to keep it really
good. But I wanted to take control over the Vagrant machine. I use it not only for "dockering".

## Assumptions &amp; Limitations

This CLI tool and its configurations assume that Vagrant's virtual machine provider is VirtualBox. Also, it uses the
`VBoxManager` to create [transient shared folders](https://www.virtualbox.org/manual/ch04.html#sharedfolders) and to enable
them to create symbolic links. The VirtualBox's User Manual states that "[f]or security reasons the guest OS is not
allowed to create symlinks by default. If you trust the guest OS to not abuse the functionality, you can enable creation
of symlinks (...)" Thus, it is important to notice this warning &mdash; and to not abuse that functionality, for your own
safety.

## Support &amp; Contributing

If you have found any bug &#x1f41e; or don't know how to do something or ever wanted a new feature, please create an
issue in [/issues](//github.com/earaujoassis/dev-box/issues). Thank you!


## License

[MIT License](http://earaujoassis.mit-license.org/) &copy; Ewerton Assis
