<?php

// パラメータ設定有り
default_args ("hogehoge.");

// パラメータ設定無し
default_args();

function default_args($args = "default." )
{
	echo $args . "<br>";
}
?>
