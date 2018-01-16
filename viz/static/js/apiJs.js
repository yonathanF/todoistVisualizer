$(document).ready(function () {

    var $historyRange=$('#historyRange');

        
    var morrisArea=Morris.Area({
        element: 'costIncomeAreaChart',
        data: [{ date: '2010 Q1', opIncome: 2666, opCost: null },
               { date: '2010 Q2', opIncome: 2978, opCost: 2294 },
	       {date: '2010 Q3', opIncome: 2378, opCost: 3294 },
	       {date: '2010 Q4', opIncome: 3778, opCost: 9294 }],

	xkey: 'date',
        ykeys: ['opIncome', 'opCost'],
        labels: ['Operating Income', 'Operating Cost'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true,
        lineColors: ['#54cdb4', '#f7605d' ,'#1ab394'],
        lineWidth:2,
        pointSize:1,
    });

   
   //ion range selector for dashboard, updates data range
    $historyRange.ionRangeSlider({
        min: 0,  //this should be changed
	max:100,
        type: 'double',
        hasGrid: true,

	onChange:function(data){
	    //call functions that call the api and update their respective ui elements
	    start=data.fromNumber;
	    end=data.toNumber; 
	    
	    costVsIncome(start, end);
	    expenseBreakdown(start, end);
	    incomeBreakdown(start, end);
	    grossProfit(start, end);
	    netProfit(start, end);
	    operatingProfit(start, end);
	    operatingExpense(start, end);
	    employeeTable(start, end);
	    serviceTable(start, end);
	}

});

    function costVsIncome(start, end){
	var parameters={
	    startDate: start,
	    endDate:end,
	    dataRequest: "costVsIncome"
	}
	
	$.getJSON('/icare/api/', parameters,

	function(data){
	    morrisArea.setData($.parseJSON(data));
	    
	});
    }

    function expenseBreakdown(start, end){
	var parameters={
	    startDate: start,
	    endDate:end,
	    dataRequest: "expenseBreakdown"
	}
	
	$.getJSON('/icare/api/', parameters,

	function(data){
	    console.log(data);
	    
	});

    }

    function incomeBreakdown(start, end){

    }

    function grossProfit(start, end){

    }

    function netProfit(start, end){

    }

    function operatingProfit(start, end){

    }

    function operatingExpense(start, end){

    }
    
    function employeeTable(start, end){

    }

    function serviceTable(start, end){

    }


    function aveGrossProfit(){

    }

    function aveNetProfit(){

    }

    function aveOperatingProfit(){

    }

    function aveOperatingExpense(){

    }
    
    function nowGrossProfit(){

    }

    function nowNetProfit(){

    }

    function nowOperatingProfit(){

    }

    function nowOperatingExpense(){

	
    }
    

});
