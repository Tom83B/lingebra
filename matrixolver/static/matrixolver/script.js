function highlightCurrentLink(){
    var a = document.getElementsByTagName("A");
    for(var i=0;i<a.length;i++){
        if(a[i].href.split("#")[0] == window.location.href.split("#")[0]){
            a[i].style.background-color = 'rgb(0,0,0)';
        }
    }
}


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
	var rows = new Array();
	var cells = new Array();
	for (i=0; i<row_num; i++){
		rows[rows.length] = table.insertRow(i);
		cells[cells.length] = new Array();
		for (j=0; j<col_num; j++){
			if (typeof vals[i][j]=='undefined') vals[i][j] = 0;
			cells[i][j] = rows[i].insertCell(j);
			cells[i][j].innerHTML = '<input type="number" name="'+'a'+i+j+'" step="any" value='+vals[i][j]+' class=input_matrix />';
		}
	}
	old_table.parentNode.replaceChild(table, old_table);
}
