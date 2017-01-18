<?php
  // controler GPIO using php
  // argv:
  // action & PinNum
	$action = isset($_GET["action"])?$_GET["action"]:null;
	$PinNum = isset($_GET["PinNum"])?$_GET["PinNum"]:null;

	if ($action == null){
		echo "$action == null";
	}
	else if ($PinNum == null){
		echo "$PinNum == null";
	}
	else{
		if($action == "on"){
			on($PinNum);
		}
		if($action == "off"){
			off($PinNum);
		}
		
	}
	
	function on($PinNum) {
		//opened gpio eclectic
	}
	function close($PinNum) {
		//opened gpio eclectic
	}

?>
