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

    # Clone recursively
    git clone --recursive https://github.com/Alechan/dotfiles ~/dotfiles
    # Create linking script
    python create_link_script.py
    # Edit which files to link
    vim link_script.bash
    # Run the script
    bash link_script.bash


For ALMOST every file in this repo you'd like to use, there should be a
symbolic link in ~/ pointing at it. Considered making a bash script to
make it automatically but would be prone to subtle errors.

The exceptions to the rule are folders/files with names telling otherwise or obvious non-dotfiles (examples, README.md or REQS-DONT-LINK)

##Example:
    cd ~

    ln -nsf path/to/dotfiles/tmux .tmux

## Mac

## Full profile
1. Open iterm2 -> Profiles -> Other Actions ... -> Import JSON:
  iterm2_profile.json

## Specifics
1. Install iterm2
2. Load colors
  * Open iterm2 -> Profiles -> Colors -> Color Presets -> Import -> Open:
    iterm2.itermcolors

### Italic (undecided if it's better or not)

3. Load italic config
  * $ tic xterm-256color-italic.terminfo
  * Open iterm2 -> Profiles -> Terminal -> Report Terminal Type:
     xterm-256color-italic
4) Set tmux as default command

#FAQ
- I'm using rkj-repos theme in oh-my-zsh but the promt has gone crazy!

Fix: https://github.com/robbyrussell/oh-my-zsh/issues/2630

- Janus doesn't work with nvim!

    ln -nsf .vimrc .nvimrc

    ln -nsf .vim .nvim

