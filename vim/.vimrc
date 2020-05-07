" Managing backup, swap and undo files.
" Some of these files can get created 'polluting' the working directory.
" These options can be used to have them in a separate directory keeping the working directory clean. 
set backupdir = ~/.vim_backup    " Backup files, ~ prefixed files
set directory = ~/.vim_swap      " Swap files, .swp files
set undodir   = ~/.vim_undo      " Undo files, .un~

" Pick one of these options
set noundofile " No undo file
"set undofile   " Create undo file

"set mouse=a    " Enable mouse usage in certain terminals
set autochdir  " Opening a file, the base directory is set to the location of the current buffer/file

set hlsearch   " Highlight the text found during search
set ignorecase " Ignore case during find
"set smartcase  " Do smart case matching
set incsearch  " Incremental search, find as you type

"set showcmd   " Show (partial) command in status line
"set showmatch " When a bracket is inserted, briefly jump to the matching one

"set list        " Display hidden characters like tab and EOL
set number      " Show line numbers
set ruler       " Display the current cursor position (row and column) at the bottom
set wrap        " Line wrapping

" Tab settings
set tabstop=4    " Tab shifts by 4 characters
set shiftwidth=4 " Indentation shift with >> and <<
set expandtab    " Insert spaces instead of tab character

" Useful with vim diff functionality
map <F7> [c     " Jump to next diff
map <F8> ]c     " Jump to previous diff

" Windows like keys
map <C-c> "+y           " CTRL c, copy to system clipboard
map <C-x> "+d           " CTRL x, cut to system clipboard
map <C-v> "+p           " CTRL v, Paste from system clipboard
map <C-Tab> :bn<CR>     " CTRL TAB, Cycle through open files
map <C-o> :tabedit      " CTRL o, open a file in a new tab window
map <C-n> :tabnew<CR>   " CTRL n, create a new tab window

" Format Json from single line to multi-line using a Python utility
command FJ .!"C:\Opt\Python\Python37\python.exe" -m json.tool
