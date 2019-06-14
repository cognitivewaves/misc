" Managing backup, swap and undo files.
" Some of these files can get created 'polluting' the working directory.
" These options can be used to have them in a separate directory keeping the working directory clean. 
set backupdir = ~/.vim_backup    " Backup files, ~ prefixed files
set directory = ~/.vim_swap      " Swap files, .swp files
set undodir   = ~/.vim_undo      " Undo files, .un~

" Pick one of these options
set noundofile " No undo file
"set undofile   " Create undo file

"set mouse=a   " Enable mouse usage (all modes)
set autochdir  " Opening a file, the base directory is set to the location of the current buffer/file

set hlsearch   " Highlight the text found during search
set ignorecase " Ignore case during find
"set smartcase " Do smart case matching
set incsearch  " Incremental search, find as you type

"set showcmd   " Show (partial) command in status line.
"set showmatch " Show matching brackets.

"set list       " Display hidden characters like tab and EOL
set number      " Show line numbers
set ruler       " Display the current cursor position (row and column) at the bottom

set tabstop=4    " Tab shifts by 4 characters
set shiftwidth=4 " Indentation shift with >> and <<
set expandtab    " Insert spaces instead of tab character

" Useful with vim diff functionality
map <F7> [c     " Jump to next diff
map <F8> ]c     " Jump to previous diff

" Windows like keys for tabbed windows
map <C-o> :tabe         " CTRL o to open a file in a new tab window
map <C-n> :tabnew<CR>   " CTRL n to create a new tab window
map <C-Tab> :tabn<CR>   " Shift to next tab window (only in gvim)
