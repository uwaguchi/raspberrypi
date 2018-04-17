#!/usr/bin/perl

# LINE通知スクリプト
$LINENotify = "/home/uwaguchi/raspberrypi/LINEnotify/LINENotify_jibun.sh";
# 設定ファイル名
$configname = "/home/uwaguchi/raspberrypi/chirashiChecker/chirashi.conf";
# 設定データ配列
my @config;

# 設定ファイル読み込み
open(CONFIG, $configname) or die("open config error for reading.");
while( my $curline = <CONFIG>){
    chomp( $curline );
    my @curdat = split( /\t/, $curline );
    push( @config, \@curdat );
}
close(CONFIG);

# 対象チラシを順に処理
foreach my $curdat( @config ){
    # 対象URLにリクエスト
    $res = `curl -s "$$curdat[2]"`;
    # チラシの日付を取得
    if( $res =~ /<h2 class=\"chirashi_info_title\">([0-9]+)月([0-9]+)日.*<\/h2>/ ){
        # 年
        chomp( $y = `date +%Y`);
        # 月
        $m = sprintf("%02d", $1);
        # 日
        $d = sprintf("%02d", $2);
        # 合体
        $date = $y.$m.$d;
        # 設定に書かれた日付より新しいかチェック
        if( $date > $$curdat[0] ){
            # 新しかったら日付を更新
            $$curdat[0] = $date;

            # LINEに投げる
            $message = "$$curdat[1] のチラシが更新されたみたいだよ！($1月$2日版）( $$curdat[2] )";
            `$LINENotify "$message"`;
        }
    }
}


# 現在の設定ファイルをバックアップ
rename( $configname, $configname.".bak" );
# 新しい設定ファイルを作成 
open(CONFIG, ">$configname") or die("open confing error for writing.");
foreach my $curdat( @config ){
    print CONFIG $$curdat[0]."\t".$$curdat[1]."\t".$$curdat[2]."\n";
}
close(CONFIG);

exit(0);

