$("#my_form_login").submit(function(event) {
          event.preventDefault(); //prevent default action 
          // let post_url = $(this).attr("action"); //get form action url
          // let request_method = $(this).attr("method"); //get form GET/POST method
          // let data = $(this).serialize(); //Encode form elements for submission	
			var parentEle = $(this).closest(".card-body");
			var username = parentEle.find("#yourUsername").val();
			var pswd = parentEle.find("#yourPassword").val();
			var user_data = {name: username,pwd: pswd};
			$.ajax({
			  url: "login_details/",
			  type: "POST",
			  data: user_data,
			  success: function(result){console.log(result);
			  var user_type = result.user_type;
			  var db = result.db_data;
			if(user_type =="developer" && db == "empty_data") {
				location.href='dashboard/add_mobile/'
			}else if(user_type =="developer" && db == "non_empty_data"){
			location.href='dashboard'}
			else if(user_type =="admin"){
			location.href='admin_dashboard'}
		    else if(user_type =="client"){
				location.href='client_dashboard'		
			}else {
				location.href='login'
			}}
			})
			});
			
$("#my_form_register").submit(function(event) {
          event.preventDefault(); //prevent default action 
          // let post_url = $(this).attr("action"); //get form action url
          // let request_method = $(this).attr("method"); //get form GET/POST method
          // let data = $(this).serialize(); //Encode form elements for submission	
			var parentEle = $(this).closest(".card-body");
			var name = parentEle.find("#name").val();
			var email = parentEle.find("#email").val();
			var usr_location = parentEle.find("#loc").val();
			var username = parentEle.find("#username").val();
			var pswd = parentEle.find("#password").val();
			var register_data = {name: username, email : email ,loc : usr_location, username : username ,pwd: pswd};
			$.ajax({
			  url: "register_user/",
			  type: "POST",
			  data: register_data,
			  success: function(result){location.href='login'}
			})
			});
						
$("#mobile").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".card-body");
		var device_type = parentEle.find("#device_type").val();
		var mobile_model = parentEle.find("#mobile_model").val();
		var manufacturer = parentEle.find("#manufacturer").val();
		var make = parentEle.find("#make").val();
		var os_type = parentEle.find("#os_type").val();
		var device_id = parentEle.find("#device_id").val();
		var serial_number = parentEle.find("#serial_number").val();
		var ip_address = parentEle.find("#ip_address").val();
		var loc = parentEle.find("#location").val();
		var pur_date = parentEle.find("#pur_date").val();
		var server_name = parentEle.find("#server_name").val();
		var phn_num = parentEle.find("#phn_num").val();
		var mobile_data = {device_type: device_type, mobile_model : mobile_model ,manufacturer : manufacturer, make : make ,os_type: os_type,device_id:device_id,serial_number:serial_number,ip_address:ip_address,loc:loc,pur_date:pur_date,server_name:server_name,phn_num:phn_num};	
        $.ajax({
              url: post_url,
              type: request_method,
              data: mobile_data,
			  success: function(response){alert("mobile added!");}
            })
	    this.reset();
        });

$("#server").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".card-body");
		var server_type = parentEle.find("#server_type").val();
		var model_type = parentEle.find("#model_type").val();
		var manufacturer = parentEle.find("#manufacturer").val();
		var make = parentEle.find("#make").val();
		var device_id = parentEle.find("#device_id").val();
		var serial_number = parentEle.find("#serial_number").val();
		var ip_address = parentEle.find("#ip_address").val();
		var server_capacity = parentEle.find("#server_capacity").val();
		var loc = parentEle.find("#location").val();
		var pur_date = parentEle.find("#pur_date").val();
		var server_data = {server_type: server_type, model_type : model_type ,manufacturer : manufacturer, make : make ,device_id:device_id,serial_number:serial_number,ip_address:ip_address,server_capacity:server_capacity,loc:loc,pur_date:pur_date};	
        $.ajax({
              url: post_url,
              type: request_method,
              data: server_data,
			  success: function(response){alert("server added!");}
            })
	    this.reset();
        });
		
$("#edit_mobile").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".card-body");
		console.log(parentEle);
		var device_type = parentEle.find("#device_type").val();
		var mobile_model = parentEle.find("#mobile_model").val();
		var manufacturer = parentEle.find("#manufacturer").val();
		var make = parentEle.find("#make").val();
		var os_type = parentEle.find("#os_type").val();
		var device_id = parentEle.find("#device_id").val();
		var serial_number = parentEle.find("#serial_number").val();
		var ip_address = parentEle.find("#ip_address").val();
		var loc = parentEle.find("#location").val();
		var pur_date = parentEle.find("#pur_date").val();
		var server_name = parentEle.find("#server_name").val();
		var phn_num = parentEle.find("#phn_num").val();
		var edit_mobile_data = {device_type: device_type, mobile_model : mobile_model ,manufacturer : manufacturer, make : make ,os_type: os_type,device_id:device_id,serial_number:serial_number,ip_address:ip_address,loc:loc,pur_date:pur_date,server_name:server_name,phn_num:phn_num};	
		console.log(edit_mobile_data);
        $.ajax({
              url: post_url,
              type: request_method,
              data: edit_mobile_data,
			  success: function(response){alert("mobile updated!");}
            })
	    // this.reset();
        });
		
$("#edit_server").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".card-body");
		console.log(parentEle);
		var device_type = parentEle.find("#device_type").val();
		var mobile_model = parentEle.find("#mobile_model").val();
		var manufacturer = parentEle.find("#manufacturer").val();
		var make = parentEle.find("#make").val();
		var capacity = parentEle.find("#capacity").val();
		var device_id = parentEle.find("#device_id").val();
		var serial_number = parentEle.find("#serial_number").val();
		var ip_address = parentEle.find("#ip_address").val();
		var loc = parentEle.find("#location").val();
		var pur_date = parentEle.find("#pur_date").val();
		var edit_server_data = {device_type: device_type, mobile_model : mobile_model ,manufacturer : manufacturer, make : make ,capacity: capacity,device_id:device_id,serial_number:serial_number,ip_address:ip_address,loc:loc,pur_date:pur_date};
        $.ajax({
              url: post_url,
              type: request_method,
              data: edit_server_data,
			  success: function(response){alert("server updated!");}
            })
	    // this.reset();
        });		
		
$("#request_mobile").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".table");
		console.log(parentEle);
		var device_type = parentEle.find("#m_type").html();
		var mobile_model = parentEle.find("#m_model").html();
		var os = parentEle.find("#m_os").html();
		var device_id = parentEle.find("#m_device_id").html();
		var days = parentEle.find("#days").val();
		var req_mobile_data = {device_type: device_type, mobile_model : mobile_model ,os : os,device_id:device_id,days:days}; 
		$.ajax({
              url: post_url,
              type: request_method,
              data: req_mobile_data,
			  success: function(response){alert("mobile requested!");}
            })
	    // this.reset();
        });				
		
$("#request_server").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".table");
		console.log(parentEle);
		var device_type = parentEle.find("#s_type").html();
		var mobile_model = parentEle.find("#s_model").html();
		var device_id = parentEle.find("#s_device_id").html();
		var days = parentEle.find("#days").val();
		var req_server_data = {device_type: device_type, mobile_model : mobile_model,device_id:device_id,days:days}; 
		$.ajax({
              url: post_url,
              type: request_method,
              data: req_server_data,
			  success: function(response){alert("server requested!");}
            })
	    // this.reset();
        });					
		
$("#allotment_request").submit(function(event) {
		event.preventDefault(); //prevent default action 
		var post_url = $(this).attr("action"); //get form action url
		console.log(post_url);
		var request_method = $(this).attr("method"); //get form GET/POST method
		var parentEle = $(this).closest(".card-body");
		console.log(parentEle);
		var user_id = parentEle.find("#user_id").val();
		var device_type = parentEle.find("#device_type").val();
		var types = parentEle.find("#types").val();
		var model = parentEle.find("#model").val();
		var os = parentEle.find("#os").val();
		var device_id = parentEle.find("#device_id").val();
		var number_days = parentEle.find("#number_days").val();
		var request_date = parentEle.find("#request_date").html;
		var req_procurred_data = {user_id:user_id,device_type: device_type, types:types,model:model,os:os,device_id:device_id,number_days:number_days}; 
		console.log(req_procurred_data);
		$.ajax({
              url: post_url,
              type: request_method,
              data: req_procurred_data,
			  success: function(response){alert(" procurred data requested!");}
            })
	    this.reset();
        });				
		
// $("#my_button").click(function(event) {
		// event.preventDefault(); //prevent default action 
		// var post_url = $(this).attr("action"); //get form action url
		// var request_method = $(this).attr("method"); //get form GET/POST method
		// var parentEle = $(this).closest("form");
		// var data = parentEle.serialize(); //Encode form elements for submission	
		// console.log(data);
		// $.ajax({
		  // url: post_url,
		  // type: request_method,
		  // data: data,
		  // success: function(result){}
		// })
		// });		