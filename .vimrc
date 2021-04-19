syntax on 
let mapleader=" "

set backspace=indent,eol,start
set hlsearch
set incsearch
set number
set relativenumber
set cursorline
set wrap
set wildmenu
set ignorecase
set smartcase

map Q :wq!<CR>
map = n
map - N

noremap <LEADER><CR> :nohlsearch<CR>

call plug#begin('~/.vim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'preservim/nerdtree'
Plug 'kshenoy/vim-signature'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'ycm-core/YouCompleteMe'
call plug#end()

let g:UltiSnipsExpandTrigger="<c-o>"
let g:UltiSnipsJumpForwardTrigger="<c-o>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"
let g:UltiSnipsSnippetDirectories = [$HOME.'/.vim/UltisnipsInsert',"UltiSnips"]
