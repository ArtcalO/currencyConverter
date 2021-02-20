		$(document).ready(function(){
			$("#search").on("keyup", function() {
				var value = $(this).val().toLowerCase();
				$("#myTable tr").filter(function() {
				$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
				});
			});
		});
		function myFunction() {
		  /* Get the text field */
		  var copyText = document.getElementById("myInput");

		  /* Select the text field */
		  copyText.select();
		  copyText.setSelectionRange(0, 99999); /* For mobile devices */

		  /* Copy the text inside the text field */
		  document.execCommand("copy");

		  /* Alert the copied text */
		} 

		function separatedNumber(x) {
        return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
   		 };
		jQuery(document).ready(function($) {

			function displayBtn(){
				let x = $('#id_amount').val()
				x.length > 2 ? $('#userInfo').show() : ('#userInfo').hide()

			};

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
			function reverseValue(str_value){
				if(str_value.includes('/')){
					var splited_string = str_value.split('/');
					return parseFloat(splited_string[1]);
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

			function splitValues(str_data){
				var data_list = str_data.split('|');
				return data_list;
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


			function senderAction(){
				var amount = parseFloat($("#inputSender").val());
				if(amount){
					$("#messageSender").show();
					var values_sender = $("#fromToSender").val();
					var values_sender_splited = splitValues(values_sender);
					var value_from = getValue(values_sender_splited[0]);
					var value_to = getValue(values_sender_splited[1]);
					var final_amount = amount*value_from/value_to;
					$("#displaySend").text(''+separatedNumber(final_amount)+'	BIF');
				}
				else {
					$("#displaySend").text('0');
					$("#messageSender").hide();
				}
				
			};

			function recieverAction(){
				var amount = parseFloat($("#inputReciever").val());
				if(amount){
					$("#messageReciever").show();
					var values_sender = $("#fromToReciever").val();
					var values_sender_splited = splitValues(values_sender);
					var value_from = reverseValue(values_sender_splited[0]);
					var final_amount = amount/value_from;
					$("#displayReciever").text(''+separatedNumber(final_amount.toFixed(2))+'	CAD');
				}
				else {
					$("#displayReciever").text('0');
					$("#messageReciever").hide();
				}
			};
			
		  $("#id_amount").keyup(actionDone);
		  $("#id_amount").keyup(displayBtn);
		  $("#id_country_to").change(actionDone);
		  $("#id_country_from").change(actionDone);
		  $("#wantSendBtn").click(function(){
		  	$("#converterDiv").hide();
		  	$("#wantRecieveDiv").hide();
		  	$("#wantSendDiv").show();
		  });
		  $("#wantRecieveBtn").click(function(){
		  	$("#wantSendDiv").hide();
		  	$("#converterDiv").hide();
		  	$("#wantRecieveDiv").show();
		  });
		 
		  $(".prev").click(function(){
		  	$("#converterDiv").show();
		  	$("#wantRecieveDiv").hide();
		  	$("#wantSendDiv").hide();
		  })
		  $("#inputSender").keyup(senderAction);
		  $("#inputReciever").keyup(recieverAction);
		});
