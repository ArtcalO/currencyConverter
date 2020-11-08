
		function separatedNumber(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
   		 };
		jQuery(document).ready(function($) {
			function getChangedItemFrom(id){
				var list = document.getElementById(id);
				var data = list.options[list.selectedIndex].innerHTML;
				return data.split(' ')[1];
			};
			function getValue(str_value){
				if(str_value.includes('/')){
					var splited_string = str_value.split('/');
					return parseFloat(splited_string[0])/parseFloat(splited_string[1]);
				}else{
					return parseFloat(str_value);
				}
			};
			function reset(){
				$("#total").text('');
			    $("#total_currency").text('');
			    $("#input").text('');
			    $("#input_currency").text('');
			    $("#value_to").text('');
			    $("#c_from").text('');
			    $("#c_to").text('');
			};
			function tauxValue(str_from, str_to){
				if(str_from.includes('/') && str_to.includes('/')){
					return (parseFloat(str_to.split('/')[1])/parseFloat(str_from.split('/')[1])).toFixed(4);
				}
				if(str_from.includes('/')){

					return (parseFloat(str_to)/parseFloat(str_from.split('/')[1])).toFixed(4);
				}else{
					return (parseFloat(str_to.split('/')[1])/parseFloat(str_from)).toFixed(4);
				}

			};

			function actionDone(){
				var form_id = 'id_country_from';
				var to_id = 'id_country_to';
				var c_from = getChangedItemFrom(form_id);
				var c_to = getChangedItemFrom(to_id);
				var from = getValue($("#id_country_from").val());
			    var to = getValue($("#id_country_to").val());
			    var x = parseFloat($("#id_amount").val());
			    var value_to = tauxValue($('#id_country_from').val(), $('#id_country_to').val());
			    if(x){
			    	var new_amount = parseFloat($(this).val())*from/to;
				    $("#total").text(separatedNumber(new_amount.toFixed(4)));
				    $("#total_currency").text(c_to);
				    $("#input").text(separatedNumber(x));
				    $("#input_currency").text(c_from);
				    (from == to) ? $("#value_to").text('1') : $("#value_to").text(separatedNumber(value_to));
				    $("#c_from").text(c_from);
				    $("#c_to").text(c_to);
			    }else{
			    	reset();
			    }
			    
			};
			
		  $("#id_amount").keyup(actionDone);
		  $("#id_country_to").change(actionDone);
		  $("#id_country_from").change(actionDone);
		});
