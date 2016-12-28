# Mydotfiles
## IMPORTANT:
Couldn't include janus as it assumes it's installed in ~/.vim. Included
only .vim.after and .vim.before

#Requisites:
- zsh
- tmux
- janus (intented to be added in the future instead of being requisite)
- vim 

#Includes:
- oh-my-zsh
- tmux custom config and plugins: tmux-sensible, tmux-yank, tpm
- [gruvbox vim theme](https://github.com/morhetz/gruvbox)

#How to
    git clone --recursive https://github.com/Alechan/dotfiles ~/dotfiles

For ALMOST every file in this repo you'd like to use, there should be a
symbolic link in ~/ pointing at it. Considered making a bash script to
make it automatically but would be prone to subtle errors.

The exceptions to the rule are folders/files with names telling otherwise or obvious non-dotfiles (examples, README.md or REQS-DONT-LINK)

##Example:
    cd ~

    ln -nsf path/to/dotfiles/tmux .tmux

#FAQ
- I'm using rkj-repos theme in oh-my-zsh but the promt has gone crazy!

Fix: https://github.com/robbyrussell/oh-my-zsh/issues/2630

- Janus doesn't work with nvim!

    ln -nsf .vimrc .nvimrc

    ln -nsf .vim .nvim

