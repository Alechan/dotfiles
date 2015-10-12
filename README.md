# dotfiles
(Couldn't include janus as it assumes it's installed in ~/.vim. Included
only .vim.after and .vim.before)
#How to
For every file in this repo you'd like to use, there should be a
symbolic link in ~/ pointing at it. Considered making a bash script to
make it automatically but would be prone to subtleties.
##Example:
    cd ~
    ln -nsf path/to/dotfiles/tmux .tmux
