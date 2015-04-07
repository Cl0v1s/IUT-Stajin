<!DOCTYPE html>
<html>

<head>
    <title>Stajin</title>
    <meta lang="fr" http-equiv="Content-Language" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <link rel="stylesheet" media="screen" type="text/css" href="/static/css/fonts.css" />
    <link rel="stylesheet" media="screen" type="text/css" href="/static/css/views/index.css" />

    <script type="text/javascript" src="/static/js/lib/jquery/jquery.js"></script>
    <script type="text/javascript" src="/static/js/lib/jquery/jquery.mousewheel.min.js"></script>
    <script type='text/javascript' src="/static/js/lib/highcharts/highcharts.js"></script>

    <script type="text/javascript" src="/static/js/views/index.js"></script>


    <script type="text/javascript">
    $(document).ready(function(){
        $('#stage-years').highcharts({
            title: {
                text: 'Evolution du nombre de stage par année universitaire'
            },
            xAxis: {
                categories: 
                [
                    % for s in stageByYear: 
                        % if s[0] !=  '':
                            '{{s[0]}}',
                        % end
                    % end 
                ]
            },
            yAxis: {
                title: {
                    text: 'Nombre de stages'
                }
            },
            series: [{
                name: "Nombre de stages",
                data: [
                    % for s in range(len(stageByYear)): 
                        % if stageByYear[s][1] !=  '' and s != 0:
                            {{stageByYear[s][1]}},
                        % end
                    % end 
                ]
            }]
        });

        $('#stage-teacher').highcharts({
            title: {
                text: 'Evolution du nombre de stage par enseignant'
            },
            xAxis: {
                categories: [
                    % for s in stageByTeacher["years"]: 
                        % if s !=  '':
                            '{{s}}',
                        % end
                    % end 
                ]
            },
            yAxis: {
                title: {
                    text: 'Nombre de stages'
                }
            },
            series: [
                % for k in stageByTeacher.keys():
                    % if k != "years" and k !="" :
                        {
                            name:'{{k}}',
                            data:
                            [
                                % for v in stageByTeacher[k]:
                                    % if v[0] != '':
                                        {{v[1]}},
                                    % end
                                % end
                            ]
                        },
                    % end
                % end
            ]
        });

        $('#stage-enterprise').highcharts({
            title: {
                text: 'Evolution du nombre de stage par entreprise'
            },
            xAxis: {
                categories: [
                    % for s in stageByEnterprise["years"]: 
                        % if s !=  '':
                            '{{s}}',
                        % end
                    % end 
                ]
            },
            yAxis: {
                title: {
                    text: 'Nombre de stages'
                }
            },
            series: [
                % for k in stageByEnterprise.keys():
                    % if k != "years" and k !="" :
                        {
                            name:'{{k}}',
                            data:
                            [
                                % for v in stageByEnterprise[k]:
                                    % if v[0] != '':
                                        {{v[1]}},
                                    % end
                                % end
                            ],
							visible: false,
                        },
                    % end
                % end
            ]
        });
    });
    </script>



</head>

<body>

    <div class="block">
        <div id="index">
            <div class="title">
                <h1>Stajin</h1>
            </div>

            <div id="intro">
                <h2>Bienvenue sur Stajin,<br>l'application de gestion de stages<br>du département Informatique de l'IUT de Bordeaux.</h2>
            </div>
        </div>
    </div>

    <div class="block">
        <div id="key-numbers">
            <div class="title">
                <h1>Chiffres clés</h1>
            </div>
            <!--Nombre de stages en cours-->
            <h1 id="stage-number">
                {{stageNumber}}
                <span>Stages en cours</span>
            </h1>
            <!--Nombre d'entreprises participantes-->
            <h2 id="enterprise-number">
                {{enterprisesNumber}}
                <span>Entreprises participantes</span>
            </h2>
            <!--Nombre d'enseignant-->
            <h2 id="teacher-number">
                {{teacherNumber}}
                <span>Professeurs encadrant</span>
            </h2>
            <!--Nombre d'étudiants-->
            <h2 id="student-number">
                {{studentNumber}}
                <span>Etudiants</span>
            </h2>

        </div>
    </div>

    <!--Slider présentant les différents graphiques-->
    <div id="slider">
        <div class="title">
            <h1>Statistiques</h1>
        </div>
        <div id="slider-previous">
           <span class="helper"></span><img src="/static/image/arrow-btn.png">
        </div>
        <div id="slider-next">
            <span class="helper"></span><img src="/static/image/arrow-btn.png">
        </div>

        <ul>
            <li>
                <div class="slider-item">
                    <div id="stage-years-container">
                        <h1>Evolution du nombre de stage par année universitaire</h1>
                        <div id="stage-years"></div>
                    </div>
                </div>
            </li>

            <li>
                <div class="slider-item">
                    <div id="stage-teacher-container">
                        <h1>Evolution du nombre de stages par enseignant</h1>
                        <div id="stage-teacher"></div>
                    </div>
                </div>
            </li>

            <li>
                <div class="slider-item">
                    <div id="stage-enterprise-container">
                        <h1>Evolution du nombre de stages par entreprise</h1>
                        <div id="stage-enterprise"></div>
                    </div>
                </div>
            </li>
        </ul>


    </div>