var arr_station_list
var station_sort = []
var station_sort_name = []
var station_sort_count =[]
var station_sort = [];
i = 0
$.ajax({
    url: '/api_lm_dashboard/',
    type: 'GET',
    success: function (result) {
    arr_station_list = (result['station_type_sum'])
    
    for (var vx in arr_station_list) 
    {
        station_sort.push([vx, arr_station_list[vx]]);
    }

    station_sort.sort(function(a, b) 
    {
        return a[1] - b[1];
    });
    
    varx = ""
    $.each(result['station_type_sum'], function (index, val)
    {
        i +=1
        varx += "<p>"+ i + "." + index + " : " + val + "</p>"
        return varx
    })
    
    $("#station_type_sum").html(varx)

    $.each(station_sort, function (x, z)
         {
            station_sort_name.push(x)
            station_sort_count.push(z)
        })
   console.log(station_sort_name)
   console.log(station_sort_count)
   
    }
   
})

