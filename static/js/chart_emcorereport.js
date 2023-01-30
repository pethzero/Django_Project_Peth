var station_list2 = []
var station_name2 = []
var station_count2 = []
var rgbColorX = [];
var color_count = 0
$.ajax({
    url: '/api_lm_dashboard/',
    type: 'GET',
    success: function (result) {

        function colorGenX() {
            var generateColor = Math.floor(Math.random() * 256);
            return generateColor;
        }

        station_list2 = (result['station_type_sum'])
        $.each(station_list2, function (var_station_name2, var_station_count2)
         {
            station_name2.push(var_station_name2)
            station_count2.push(var_station_count2)
        })

        for (var k = 0; k < color_count; k += 1) {
            if (k == 0) {
                rgbColorX.push('rgba(' + 245 + ',' + 99 + ',' + 120 + ','+ 0.6 + ')');
            }
            else if (k == 1) {
                rgbColorX.push('rgba(' + 255 + ',' + 99 + ',' + 71 + ','+ 0.4 + ')');
            }
            else if (k == 2) {
                rgbColorX.push('rgba(' + 255 + ',' + 99 + ',' + 120 + ','+ 0.4 + ')');
            }
            else if (k == 3) {
                rgbColorX.push('rgba(' + 255 + ',' + 102 + ',' + 120 + ','+ 0.6 + ')');
            }
            else if (k == 4) {
                rgbColorX.push('rgba(' + 255 + ',' + 102 + ',' + 138 + ','+ 0.6 + ')');
            }
            else if (k == 5) {
                rgbColorX.push('rgba(' + 255 + ',' + 102 + ',' + 150 + ','+ 0.7 + ')');
            }
            else if (k == 6) {
                rgbColorX.push('rgba(' + 255 + ',' + 102 + ',' + 170 + ','+ 0.8 + ')');
            }
            else if (k == 7) {
                rgbColorX.push('rgba(' + 255 + ',' + 120 + ',' + 200 + ','+ 0.8 + ')');
            }
        }

        let Ax = document.getElementById('zx').getContext('2d');
        let Vx = new Chart(Ax,
            {
                animationEnabled: true,
                type: 'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea

                data: {
                    labels: station_name2,     //  ชื่อตัวแปรในแนวนอน,     
                    datasets: [{
                        data: station_count2, // ชื่อตัวแปรในแนวตั้ง,
                        backgroundColor: rgbColorX,
                        

                    }],
                    
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    title: {
                        display: true,
                        text: 'Data Station X',
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
