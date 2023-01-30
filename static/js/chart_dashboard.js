var station_list = []
var station_name = []
var station_count = []
var rgbColor = [];
var color_count = 0
$.ajax({
    url: '/api_lm_dashboard/',
    type: 'GET',
    success: function (result) {

        function colorGen() 
        {
            var generateColor = Math.floor(Math.random() * 256);
            return generateColor;
        }
        $("#station_sum_of_all").html(result['station_sum_of_all'])
        station_list = (result['station_type_sum'])
        $.each(station_list, function (var_station_name, var_station_count) 
        {
            station_name.push(var_station_name)
            station_count.push(var_station_count)
            color_count += 1
        })
        


        for (var k = 0; k < color_count; k += 1) {
            if (k == 0) {
                rgbColor.push('rgba(' + 239 + ',' + 45 + ',' + 45 + ')');
            }
            else if (k == 1) {
                rgbColor.push('rgba(' + 255 + ',' + 239 + ',' + 45 + ')');
            }
            else if (k == 2) {
                rgbColor.push('rgba(' + 49 + ',' + 210 + ',' + 49 + ')');
            }
            else if (k == 3) {
                rgbColor.push('rgba(' + 46 + ',' + 255 + ',' + 228 + ')');
            }
            else if (k == 4) {
                rgbColor.push('rgba(' + 5 + ',' + 0 + ',' + 162 + ')');
            }
            else if (k == 5) {
                rgbColor.push('rgba(' + 255 + ',' + 46 + ',' + 235 + ')');
            }
            else if (k == 6) {
                rgbColor.push('rgba(' + 252 + ',' + 176 + ',' + 45 + ')');
            }
            else if (k == 7) {
                rgbColor.push('rgba(' + 34 + ',' + 118 + ',' + 12 + ')');
            }
            else if (k == 8) {
                rgbColor.push('rgba(' + 5 + ',' + 0 + ',' + 162 + ')');
            }
            else if (k == 9) {
                rgbColor.push('rgba(' + 137 + ',' + 32 + ',' + 198 + ')');
            }
            else if (k == 10) {
                rgbColor.push('rgba(' + 255 + ',' + 60 + ',' + 0 + ')');
            }
            else {
                rgbColor.push('rgba(' + colorGen() + ',' + colorGen() + ',' + colorGen() + ')');
            }
        }

        let Zero = document.getElementById('myChart').getContext('2d');
        let ZeroChart = new Chart(Zero,
            {
                animationEnabled: true,
                type: 'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea

                data: {
                    labels: station_name,     //  ชื่อตัวแปรในแนวนอน,     
                    datasets: [{
                        data: station_count, // ชื่อตัวแปรในแนวตั้ง,
                        backgroundColor:[
                    'rgba(255, 99, 132, 0.6)',
                    'rgba(54, 162, 235, 0.6)',
                    'rgba(255, 206, 86, 0.6)',
                    'rgba(75, 192, 192, 0.6)',
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(255, 99, 132, 0.6)'
                ],
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    title: {
                        display: true,
                        text: 'Data Station Current',
                        fontSize: 25
                    },
                    legend: {
                        display: false,

                    },
                    layout: {
                        padding: {
                            left: 0,
                            right: 40,
                            bottom: 0,
                            top: 0
                        }
                    },
                    tooltips: {
                        enabled: true
                    },
                    scales: {
                        xAxes: [{
                         // barPercentage: 1.25
                        }]
                    }
                }
            });
    }
})
