// /**
//  * Created by Jean-Claude on 2017-07-31.
//  */
//

$(document).ready(function() {

    $.ajax({
        type: 'GET',
        url: '/dashboard_stats'
    })
            .done(function (response) {
                console.log(response);

                $('#hours_worked').text(response.total_parsed);
                $('#hours_left').text(Math.round((755 - response.total) * 100) / 100);
                $('#time_entries').text(response.total_entries);
                $('#days_tracked').text(response.days_tracked + "+");
                $('#hours_this_month').text(response.hours_this_month + "+ Hours");

                var canvasWidth = 800;
                var canvasHeight = 400;
                var smallRadius = "30%";
                var bigRadius = "90%";
                var general = "VCH General";
                var im = "Inventory Management";
                var hiv = "HIV Database";
                var tb = "TB Database";
                var cd = "CD Database";

                var chart_width = $('#pieChart').width();

                if (screen.width < 768){
                    canvasWidth = chart_width;
                    canvasHeight = 400;
                    smallRadius = "15%";
                    bigRadius = "80%";
                    general = "VCH";
                    im = "IM";
                    hiv = "HIV";
                    tb = "TB";
                    cd = "CD";
                }

                var pie = new d3pie("pieChart", {
                    "header": {
                        "title": {
                            "text": response.from_date + " to " + response.today,
                            "fontSize": 24,
                            "font": "open sans",
                            "color": "#ef5350"
                        },
                        "subtitle": {
                            "text": "",
                            "color": "#449d44",
                            "fontSize": 15,
                            "font": "open sans"
                        },
                        "titleSubtitlePadding": 0
                    },
                    "size": {
                        "canvasWidth": canvasWidth,
                        "canvasHeight": canvasHeight,
                        "pieInnerRadius": smallRadius,
                        "pieOuterRadius": bigRadius
                    },
                    "data": {
                        "sortOrder": "value-desc",
                        "content": [
                            {
                                "label": general,
                                "value": response.General,
                                "color": "#1ee675",
                            },
                            {
                                "label": im,
                                "value": response.IM,
                                "color": "#daca61"
                            },
                            {
                                "label": tb,
                                "value": response.TB,
                                "color": "#2081c1"
                            },
                            {
                                "label": cd,
                                "value": response.CD,
                                "color": "#e98125"
                            },
                            {
                                "label": hiv,
                                "value": response.HIV,
                                "color": "#cd29eb"
                            }
                        ]
                    },
                    "labels": {
                        "outer": {
                            "pieDistance": 32
                        },
                        "inner": {
                            "hideWhenLessThanPercentage": 3
                        },
                        "mainLabel": {
                            "fontSize": 15
                        },
                        "percentage": {
                            "color": "#ffffff",
                            "decimalPlaces": 0,
                            "fontSize": 15
                        },
                        "value": {
                            "color": "#adadad",
                            "fontSize": 15
                        },
                        "lines": {
                            "enabled": true
                        }
                    },
                    "tooltips": {
                        "enabled": true,
                        "type": "placeholder",
                        "string": "{label}: {value} Hours, {percentage}%",
                        "styles": {
                            "fadeInSpeed": 255,
                            "backgroundOpacity": 0.79
                        }
                    },
                    "effects": {
                        "pullOutSegmentOnClick": {
                            "effect": "none",
                            "speed": 400,
                            "size": 8
                        }
                    },
                    "misc": {
                        "gradient": {
                            "enabled": true,
                            "percentage": 100
                        }
                    },
                    "callbacks": {
                        "onMouseoverSegment": null,
                        "onMouseoutSegment": null,
                        "onClickSegment": null
                    }
                });
        });
    });