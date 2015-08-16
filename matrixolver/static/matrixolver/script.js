function createInputTable(row_num, col_num, vals){
	if (typeof vals=='undefined'){
		vals = new Array();
		for (i=0; i<row_num; i++){
			vals[i] = Array.apply(null, Array(col_num)).map(Number.prototype.valueOf,0);
		}
	}
	var form = document.createElement('form')
	var old_table = document.getElementById('InputTable')
	var table = document.createElement('table')
	table.id = 'InputTable';
	table.className = 'table table-bordered table-condensed';
	var rows = new Array();
	var cells = new Array();
	for (i=0; i<row_num; i++){
		rows[rows.length] = table.insertRow(i);
		cells[cells.length] = new Array();
		for (j=0; j<col_num; j++){
			if (typeof vals[i][j]=='undefined') vals[i][j] = 0;
			cells[i][j] = rows[i].insertCell(j);
			name = 'a'+i+j
			cells[i][j].innerHTML = "<input class='form-control cInput' type='text' name='"+name+"' onclick='select()' step='any' value='"+vals[i][j]+"' autocomplete='off' />";
		}
	}
	old_table.parentNode.replaceChild(table, old_table);
}

function createSysInputTable(row_num, col_num, vals){
	if (typeof vals=='undefined'){
		vals = new Array();
		for (i=0; i<row_num; i++){
			vals[i] = Array.apply(null, Array(col_num)).map(Number.prototype.valueOf,0);
		}
	}
	var form = document.createElement('form')
	var old_table = document.getElementById('InputTable')
	var table = document.createElement('table')
	table.id = 'InputTable';
	table.className = 'table table-bordered table-condensed';
	var rows = new Array();
	var cells = new Array();
	for (i=0; i<row_num; i++){
		rows[rows.length] = table.insertRow(i);
		cells[cells.length] = new Array();
		for (j=0; j<col_num+1; j++){
			if (typeof vals[i][j]=='undefined') vals[i][j] = 0;
			cells[i][j] = rows[i].insertCell(j);
			name = 'a'+i+j
			if (j!=col_num){
				cells[i][j].innerHTML = "<input class='form-control cInput' type='text' name='"+name+"' id='"+name+"' onclick='select()' step='any' value='"+vals[i][j]+"' autocomplete='off' />";}
			else{
				cells[i][j].innerHTML = "<input class='form-control cVecInput' type='text' name='"+name+"' id='"+name+"' onclick='select()' step='any' value='"+vals[i][j]+"' autocomplete='off' />";}
		}
	}
	old_table.parentNode.replaceChild(table, old_table);
}
