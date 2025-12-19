# Git Tutorial



## Setup
To use git, you (obviously) need [git](https://git-scm.com/download/win) first. You can download it using the link, following the instructions.

For this tutorial, it is assumed that you are using [VSCode](https://code.visualstudio.com/download) and using a Windows Operating System.

## SSH (Secure SHell)
(Taken from [https://compeng-gg.github.io/2025-fall-ece344-docs/setup-lab0/](https://compeng-gg.github.io/2025-fall-ece344-docs/setup-lab0/))

We're going to generate SSH keys for you. This is a secure way to connect to servers, and for servers to verify that the key belongs to you. An SSH key has two parts, a private key and a public key. Only you should have access to the private key, it's used to encrypt your data. Never share your private key. You can give out your public key, it's used to identify you (we're going to register it on GitHub).

Launch **Git Bash** by pressing the Windows key and typing `Git Bash`, then pressing enter. This is your terminal.

Older guides may as you to generate an RSA key, but current best practices suggest upgrading to Ed25519 (this is the cryptography). Generate your new key by typing the following command in your terminal and pressing enter:

```bash
ssh-keygen -t ed25519
```

You can follow these steps:

1. Press enter to save your private key to the default location.
2. Enter a passphrase. **Enter a good passphrase and remember it**. This should be unique, and not shared with any other of your passwords. It's important to set this because even if you accidentally share your private key (which you should NEVER do), someone else would still need your passphrase to use it and pretend to be you. If you'd like to ignore this warning, you can make it blank (as someone who has done this, trust me, you'll regret it).
3. Enter the same passphrase again to make sure you typed it correctly.
That's it! You should get a message that your key was successfully created. There's going to be two files generated: `id_ed25519`, and `id_ed25519.pub`. `id_ed25519` contains your private key, you should **NEVER** share this and be very careful if you try to move it. This key is your secure identity, you should be able to use this to access multiple systems if you keep it safe. `id_ed25519.pub` contains your public key, and we'll use this.

Type the following command and press enter:
```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the result of this command, this is your public key. You'll need it to access the git repository.

Before moving on, please setup an SSH agent so you don't have to type a passphrase everytime. You'll need it even if you don't have a passphrase for a smooth experience. Follow the guide provided by GitHub [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows#adding-your-ssh-key-to-the-ssh-agent)

## GitHub
(Taken from [https://compeng-gg.github.io/2025-fall-ece344-docs/setup-lab0/](https://compeng-gg.github.io/2025-fall-ece344-docs/setup-lab0/))

Now you'll have to add your SSH key to GitHub. Make sure you're logged in, we'll be adding our public key so we can access the code.

1. Click your profile photo in the top right.
2. Click on `Settings`.
3. Look for `Access` in the sidebar and click `SSH and GPG keys`.
4. Click the green `New SSH key` near the top right.
5. Type whatever you want to name this key, something like your email is fine.
6. Paste your public key into the `Key` field.
7. Click `Add SSH key`.

## Basic Operations
### Cloning
I know this section looks super long and complicated. You only need to do these steps once per repository. 

First we need to do a **clone** of the repository so we have a copy on our own computers to work with. A clone simply takes the repository and makes a copy on your local computer. Any change you make to the file will not be updated in the global repository until you **push** those changes (see below on how to use `git push`).

Using **Git Bash** (same as before), run the following commands
```bash
cd ~
git clone https://github.com/TheMatthewDu/MIE491Y1_Capstone_Codebase.git
```

This creates a copy of the `MIE491Y1_Capstone_Codebase` repository in your `C:\Users\<USERNAME>` folder. You can move this folder to any other folder you wish. At this stage, you can close git bash.

Now open VSCode. Click `Open Folder` and open the `MIE491Y1_Capstone_Codebase` folder. Congradulations! You have just cloned your first git repository. We now want to launch a terminal so we do not need to keep using git bash. There are 3 ways to do this:
1. **Keyboard Shortcut**: Press `Ctrl + '` (backtick/tilde character)
2. **Menu Bar**: Go to `View > Terminal`
3. **Command Palette**: Open the Command Palette by pressing `Ctrl + Shift + P`. Type View: `Toggle Terminal` or `Terminal: New Terminal` and select the corresponding command from the list. 

For this particular repository, to prevent clashes, I have disabled push permissions for you to push to the `main` branch. Therefore, all changes you make will be to your own branch, then once you are done, make a `pull request`, and I will review and merge everything. Don't worry if you do not know what any of that means; the point here is that we now need to move to your own branch where you will work.

Run the following commands
```bash
git switch <Your First Name>
git config --global push.default current
```

### Git Pull
A **git pull** is when you get update your local copy of an already cloned repository with the most up-to-date files. To do so, run the following command
```bash
git pull origin main
```

It is always a good practice to pull frequently (i.e., every time you start to work) so you have the most up to date files

### Git Add
A **git add** tells git which files that you want it to monitor in the repository. When you create a new file, git by default will NOT automatically add that file to the list of files it keeps track of, so you need to add it for it to be tracked.

To add a file, run
``` bash
git add <filename>
```

### Git Commit
Once you are done editting a file, you need to `commit` it, which is to say, update a save state of the file to git. In other words, this is effectively a "save file" step. It is also customary to leave a helpful comment to help understand what each commit does.

To commit a file, run the following,
``` bash
git commit -m "<comment>"
```
This command will commit ALL of the files that have been added by ``git add``

### Git Push
Now once you are done, you want to **push** the changes to the repository so that everyone else can see it.
``` bash
git push
```
This command will add all of your commits (yes, you can have multiple commits be pushed at once). As mentioned before, this push will go to your user branch.

### Pull Requests
If you are happy with your change, we want to combine everything to the `master` branch, which will be the "good copy" of the codebase that will be used for the project. A **Pull Request** is a way of submitting a request to do something in github that others can review and leave comments on. Once everyone is happy with the pull request (often abbreviated as PR), they can approve and merge it.

To create a **Pull Request**, go to the [github repository](https://github.com/TheMatthewDu/MIE491Y1_Capstone_Codebase) and go to the `Pull Requests` tab. Press the following button.
![Pull Request Button Location](image.png)
Fill out the form, **ensuring you select the `base:main` opton**.

Submit the pull request, and then harass Matt to approve it.