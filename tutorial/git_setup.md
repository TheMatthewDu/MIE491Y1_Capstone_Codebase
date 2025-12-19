# Git Setup

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

## Cloning
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

I have created individual branches for everyone to work on so we don't accidentally overwrite someone else's work. You can think of each branch as an isolated repository within the master repository that you work in. Once you are happy with your changes, we can "copy" the changes (called a **merge**) into the master branch, which is the "good copy" of the code.

To go to your branch, run the following commands:
```bash
git switch <Your First Name>
git config --global push.default current
```

I would advise that you do NOT switch branches and always work in your own branch to prevent clashes (i.e., one person change script A which script B relies on).
