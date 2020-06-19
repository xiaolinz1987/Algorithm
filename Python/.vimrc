"基础设置
set nocompatible                "去掉vi的一致性
set number                      "显示行号
set guioptions-=r               "隐藏滚动条 
set guioptions-=L
set guioptions-=b
set showtabline=0               "隐藏顶部标签栏
set guifont=Monaco:h13          "设置字体         
syntax on                       "开启语法高亮
let g:solarized_termcolors=256  "颜色主题
set background=dark             "设置背景色
colorscheme blue
set nowrap                      "设置不折行
set fileformat=unix             "设置以unix的格式保存文件
set cindent                     "设置C样式的缩进格式
set tabstop=4                   "设置table长度
set shiftwidth=4                "同上
set showmatch                   "显示匹配的括号
set scrolloff=5                 "距离顶部和底部5行
set laststatus=2                "命令行为两行
set fenc=utf-8                  "文件编码
set backspace=2
set mouse=a                     "启用鼠标
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set ignorecase                  "忽略大小写
set incsearch
set hlsearch                    "高亮搜索项
set noexpandtab                 "不允许扩展table
set whichwrap+=<,>,h,l
set autoread
set cursorline                  "突出显示当前行
set cursorcolumn                "突出显示当前列

"按F5运行Python
nmap <F5> <Esc>:w<CR>:!clear;python3 %<CR>
"imap <F5> <Esc>:w<CR>:!clear;python3 %<CR>

"下载并安装插件
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Lokaltog/vim-powerline'
Plugin 'L9'
Plugin 'Valloric/YouCompleteMe'
call vundle#end()
filetype plugin indent on

"YouCompleteMe设置
let g:ycm_global_ycm_extra_conf='~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py'
let g:ycm_server_keep_logfiles=1                          "Log设置
let g:ycm_server_log_level='debug'
let g:ycm_confirm_extra_conf=0                            "打开vim时不再询问是否加载ycm_extra_conf.py配置
set completeopt=longest,menu
let g:ycm_path_to_python_interpreter='/usr/bin/python3' "Python解释器路径
let g:ycm_python_binary_path='/usr/bin/python3'
let g:ycm_seed_identifiers_with_syntax=1                  "开启语义补全
let g:ycm_complete_in_comments=1                          "在注释中开启补全
let g:ycm_min_num_of_chars_for_completion=2               "开始补全的字符数
let g:ycm_autoclose_preview_window_after_completion=1     "补全后自动关机预览窗口
let g:ycm_cache_omnifunc=0                                "禁止缓存匹配项，每次都重新生成匹配项
let g:ycm_complete_in_strings=1                           "字符串中也开启补全
let g:ycm_seed_identifiers_with_syntax=1                  "补全关键字
autocmd InsertLeave * if pumvisible() == 0|pclose|endif   "离开插入模式后自动关闭预览窗口
