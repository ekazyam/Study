<?php
//htmlデータを安全な文字列に変換する。
function h($htmldata){
        echo(
        	htmlspecialchars(
        		$htmldata,
			ENT_QUOTES,
			'UTF-8'
	)
	."<br>"
	);
}
?>
