#!/bin/bash

# 1. 開始メッセージを出力
# 2. パッケージインストールのメッセージを出力
# 3. yum install でパッケージをインストール
# 4. ファイルの展開のメッセージを出力
# 5. tgzファイルを展開
# 6. ファイルの配置メッセージを出力
# 7. 指定ディレクトリにファイルを配置
# 8. ファイルの置換メッセージを出力
# 9. ファイルを置換
# 10. 完了のメッセージを出力

function print_message() {

    local msg="$1"

    echo "***************************************************"
    echo ""
    echo "${msg}"
    echo ""
    echo "***************************************************"
}

function error_message_and_exit() {

    echo "インストールに失敗しました."
    exit 1
}

function install_package() {

    local package_name="$1"

    yum install -y "${package_name}"
    if [ $? -ne 0 ] ; then
        error_message_and_exit
    fi
}

function install_packages() {
    print_message "Start Install Package"
    packages=("java" "wget")
    for target in "${packages[@]}" ; do
        install_package "${target}"
    done


}

function extract_tarfile() {
    print_message "Start extract tarfile"

    tar zxvf "${PWD}/release_file.tgz"
    
    if [ $? -ne 0 ] ; then
        error_message_and_exit
    fi
    
}

function copy_files() {
    print_message "Start copy files"
    cd "${PWD}/release_file"
    local currnt_dir=$(pwd)
    for target in $(find ${currnt_dir} -type f) ; do

        src_file="${target/${currnt_dir}//opt/install}"
        src_dir="$(dirname "${src_file}")"

        if [ ! -d "${src_dir}" ] ; then
            mkdir -p "${src_dir}"
        fi

        cp "${target}" "${src_file}"

    done

}

function replace_conf() {
    print_message "Start replace config file."

    local config_file="/opt/install/conf/test.conf"

    if [ -f "${config_file}" ] ; then
        sed -i "s/0.0.0.0/255.255.255.254/g" "${config_file}"
    fi
}


function main() {

    # 1. 開始メッセージを出力
    print_message "Start Installer!!"

    # 2. パッケージインストールのメッセージを出力
    # 3. yum install でパッケージをインストール
    install_packages

    # 4. ファイルの展開のメッセージを出力
    # 5. tgzファイルを展開
    extract_tarfile

    # 6. ファイルの配置メッセージを出力
    # 7. 指定ディレクトリにファイルを配置
    copy_files

    # 8. ファイルの置換メッセージを出力
    # 9. ファイルを置換
    replace_conf

    # 10. 完了のメッセージを出力
    print_message "Install Completed"
    
}

main