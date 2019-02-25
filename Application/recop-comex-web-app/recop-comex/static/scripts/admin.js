if(window.location.pathname=='/admin/events/calendar'){
	var today = new Date()
	var month = today.getMonth() + 1
	var year = today.getFullYear()
	var first_day = new Date(year + '-' + month + '-1')
	var last_day = new Date(year, month , 0)
	var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	document.getElementById('month_year').innerHTML=months[month-1] + ' ' + year
	var calendar = Calendar(first_day, last_day, month, year)
	document.getElementById('calendar').appendChild(calendar)
}

if(window.location.pathname=='/admin/events/create'){
	document.getElementById('thrust').options.item(0).selected="True"
	document.getElementById('thrust').options.item(0).hidden="True"
	document.getElementById('select_link').options.item(0).selected="True"
	document.getElementById('select_link').options.item(0).hidden="True"
	document.getElementById('target_link').value = ""
}

if(window.location.pathname.startsWith('/admin/donations/inkind')){
	var divs=0
	document.getElementById('type_select').options.item(0).selected="True"
	document.getElementById('type_select').options.item(0).hidden="True"
}

if(window.location.pathname=='/admin/inventory/add'){
    document.getElementById('event').options.item(0).hidden=true
    document.getElementById('event').options.item(0).selected=true
}
var f = []

function check_pass()
{

    pass = document.getElementById('password')
    confirm = document.getElementById('password_confirm')

    if (pass.value!=confirm.value)
    {
        alert('Passwords did not match.')
        return false
    }
    else
    {
        return true
    }
}

function event_pages(value)
{

	info = document.getElementById('info_div')
	tracker = document.getElementById('tracker_div')
	participant = document.getElementById('participant_div')

	if (value=='info')
	{

		info.className='container'
		tracker.className='container hidden'
		participant.className='container hidden'

	}
	else if (value=='tracker')
	{

		tracker.className='container'
		info.className='container hidden'
		participant.className='container hidden'

	}
	else
	{

		participant.className='container'
		info.className='container hidden'
		tracker.className='container hidden'

	}

}

function prev_next(sender){

	document.getElementById('calendar').innerHTML=""

	if (sender=="prev") {
		month = month - 1
		if (month<1){
			month = 12
			year = year - 1
		}
	}

	if (sender=="next"){
		month = month + 1

		if (month>12){
		month = 1
		year = year + 1
		}
	}

	document.getElementById('month_year').innerHTML=months[month-1] + ' ' + year

	var calendar = Calendar(first_day, last_day, month, year)

	document.getElementById('calendar').appendChild(calendar)

}

function filter(value)
{

	sender = document.getElementById(value)

	if (sender.checked==true)
	{
		f.push(value)

		// when 'all' is selected, remove value from array
		if (f == 0 || f == 7)
		{
			f.splice(f.indexOf(value), 1);
		}
	}
	else
	{
		f.splice(f.indexOf(value), 1);
	}

	var tbody = document.getElementsByTagName('tbody')

	if (f.length!=0)
	{
		for (ctr=0; ctr<=f.length-1; ctr++)
		{
			for (ctr2=0; ctr2<=tbody.length-1; ctr2++)
			{
					// get tbodies then compare to f.length
					if (tbody[ctr2].id.indexOf(f[ctr].toString()+'_'))
					{
						tbody[ctr2].style.display="none"
					}
					else
					{ 
						tbody[ctr2].style.display=""
					}
			}
		}
	}
	else
	{
		for (ctr2=0; ctr2<=tbody.length-1; ctr2++)
		{
			tbody[ctr2].style.display=""
		}
	}
}

function add_comm(){
	div = document.getElementById('link_div')
	input = document.getElementById('select_link');
	comm = document.getElementById('target_link')
	id = input.selectedIndex
	selected = input.options.item(id).value
	text = input.options[id].text
	input.options.item(id).hidden=true
	
	if (document.getElementById(selected)){
		document.getElementById(selected).style.display=""
	}
	else{
		div.innerHTML = div.innerHTML + "<span class='tag is-dark is-small' id="+ selected + ">"+ text + "&nbsp; <a name='"+selected+"'onclick='remove_comm(this.name)'><i class='fas fa-times'></i></a></span>"
	}

	comm.value = comm.value + selected + '|'
	input.selectedIndex=0
}

function remove_comm(value){

	document.getElementById(value).style.display = "none"
	control =  document.getElementById('select_link')

	for (id=0; id<=control.options.length-1; id++){
		if (control.options.item(id).value==value){
			control.options.item(id).hidden=false
		}
		if (control.options.item(id).value=="Please Select Here"){
			control.selectedIndex=id
		}
	}

	selected = document.getElementById('target_link').value
	str = '|' + value.toString() + '|'
	removed = selected.replace(str, '')
	document.getElementById('target_link').value = removed	
	control.selectedIndex=0

}

function show_slip(value){

	a = document.getElementById(value+'_modal')
	a.style.display='block'

}

function close_slip(value){
	a = document.getElementById(value+'_modal')
	a.style.display='none'

}

function item_field(value){

	types = document.getElementById('types')
	quantities = document.getElementById('quantities')

	if (value[0]=='add'){

		type_select = document.getElementById('type_select')
		type = type_select.options[type_select.selectedIndex].text
		index = type_select.selectedIndex
		quantity = document.getElementById('quantity').value
		orig_btn = document.getElementById(value[1])
		length=type_select.length-1

		if (divs==length){

            Swal.fire({
                title: "Maximum number of item types exceeded! (Types="+length.toString()+")", 
                type: "error",
                customClass: "modal",
                buttonsStyling: false,
                allowOutsideClick: false,
                heightAuto: false,
                confirmButtonClass: 'button is-medium submit'
            })

		}

		else if (quantity=='' || type_select.selectedIndex==0 || quantity<=0){
           
            Swal.fire({
                title: "One or more fields are invalid", 
                type: "error",
                customClass: "modal",
                buttonsStyling: false,
                allowOutsideClick: false,
                heightAuto: false,
                confirmButtonClass: 'button is-medium submit'
            })

		}

		else{

			clone_btn = orig_btn.cloneNode(true)

			columns = document.createElement('div')
			columns.className='columns'

			for (ctr=0; ctr<=2; ctr++){

				column = document.createElement('div')

				field = document.createElement('div')
				field.className='field'

				control = document.createElement('div')
				control.className='control'

				if (ctr<2){
					column.className='column' 
					element=document.createElement('input')
					if (ctr==0){
						element.value = type
						element.className= 'input'
						element.setAttribute('readonly', true)
					}
					else{
						element.value = quantity
						element.className= 'input'
						element.id = index.toString() + '_qty'
						element.setAttribute('readonly', true)
					}
				}
				else{
					column.className='column is-1'
					clone_btn.id = index.toString()
					clone_btn.className='button is-danger tooltip'
					clone_btn.setAttribute('data-tooltip','Remove')
					clone_btn.innerHTML='<i class="fas fa-times-circle"></i>'
					clone_btn.name='remove'
					element = clone_btn
				}
				control.appendChild(element)
				field.appendChild(control)
				column.appendChild(field)
				columns.appendChild(column)
			}
			divs++
			columns.id=index.toString()+'_col'
			document.getElementById('fields').appendChild(columns)
			type_select.options.item(index).hidden=true
			type_select.options.item(0).selected=true
			document.getElementById('quantity').value=''
			types.value = types.value + index + '|'
			quantities.value = quantities.value + quantity + '|'
		}
	}
	else{
		type_select.options.item(value[1]).hidden=false
		
		types = document.getElementById('types')
		str = value[1].toString() + '|'
		removed = types.value.replace(str, '')
		types.value = removed
		alert(removed)

		qty = document.getElementById(value[1]+'_qty')
		quantities= document.getElementById('quantities')
		str = qty.value.toString() + '|'
		removed = quantities.value.replace(str, '')
		quantities.value = removed
		alert(removed)

		columns=document.getElementById(value[1].toString()+'_col')
		columns.remove()
		divs--

	}

	if(divs>=1){
		document.getElementById('header').style.display='block'
	}
	else{
		document.getElementById('header').style.display='none'
	}
}

function donate_choose(value){

    comm = document.getElementById('comm')
    event = document.getElementById('events')
    sponsor = document.getElementById('sponsor')
    trans_slip = document.getElementById('trans_slip')
    sel_comm = document.getElementById('sponsee')
    sel_event = document.getElementById('event')

    if (value==1){
        comm.className="column"
        events.className="hidden"
        sponsor.className="column"
        trans_slip.className="columns"
        sel_event.value=''
    }
    else{
        comm.className="hidden"
        events.className="column"
        sponsor.className="column"
        trans_slip.className="columns"
        sel_comm.value=''
    }

}

function donation(value){

    comm = document.getElementById('comm')
    event = document.getElementById('events')
    sponsor = document.getElementById('sponsor')
    trans_slip = document.getElementById('trans_slip')
    give_to = document.getElementById('give_to')
    sel_comm = document.getElementById('sponsee')
    sel_event = document.getElementById('event')
    sel_sponsor = document.getElementById('sponsor')

    if (value==1){
    	give_to.className="columns"
    }
    else{
    	give_to.className="hidden"
        comm.className="hidden"
        events.className="hidden"
        sponsor.className="hidden"
        trans_slip.className="hidden"
        sel_comm.value=''
        sel_event.value=''
        sel_sponsor.value=''
    }

}

function settingsVPACAD() {
    var div = document.getElementById("settingsACAD");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function settingsVPFMI() {
    var div = document.getElementById("settingsFMI");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function settingsPRES() {
    var div = document.getElementById("settingsSPRES");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function filtershrink() {
    var div = document.getElementById("filterDIV");
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}