//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            var checkioInput = data.in;

            if (data.error) {
                $content.find('.call').html('Fail: checkio(' + JSON.stringify(checkioInput) + ')');
                $content.find('.output').html(data.error.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
                return false;
            }

            var rightResult = data.ext["answer"];
            var userResult = data.out;
            var result = data.ext["result"];
            var result_addon = data.ext["result_addon"];


            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));

            if (!result) {
                $content.find('.call').html('Fail: checkio(' + JSON.stringify(checkioInput) + ')');
                $content.find('.answer').html('Right result:&nbsp;' + JSON.stringify(rightResult));
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: checkio(' + JSON.stringify(checkioInput) + ')');
                $content.find('.answer').remove();
            }
            //Dont change the code before it

            var canvas = new PumpingStationsCanvas($content.find(".explanation")[0], checkioInput);
            canvas.createCanvas(explanation);


            this_e.setAnimationHeight($content.height() + 60);

        });

       
        function PumpingStationsCanvas(dom, map) {
            var format = Raphael.format;

            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var cell = 40;

            var fullSizeX = map[0].length * cell,
                fullSizeY = map.length * cell;

            var paper = Raphael(dom, fullSizeX, fullSizeY, 0, 0);

            var attrAxis = {"stroke": colorBlue4, "stroke-dasharray": "- ", "stroke-width": 1};
            var attrPipe = {"stroke": colorBlue4, "stroke-width": 3};
            var attrRect = {"stroke": colorBlue4, "stroke-width": 1, "fill": colorBlue1};


            this.createCanvas = function(pipes) {
                for (var i = 0; i <= map.length; i++){
                    paper.path(format("M0,{0}H{1}", i * cell, fullSizeX)).attr(attrAxis);
                }
                for (i = 0; i <= map[0].length; i++){
                    paper.path(format("M{0},0V{1}", i * cell, fullSizeY)).attr(attrAxis);
                }
                for (var row = 0; row < map.length; row++){
                    for (var col = 0; col < map[0].length; col++){
                        if (map[row][col] === 1) {
                            paper.rect(col * cell, row * cell, cell, cell).attr(attrRect);
                        }
                    }
                }
                for (i = 0; i < pipes.length; i++) {
                    var p = pipes[i];
                    paper.path(format("M{0},{1}L{2},{3}"),
                        p[1] * cell,
                        p[0] * cell,
                        p[3] * cell,
                        p[2] * cell
                    ).attr(attrPipe);
                }
            }

        }
        //Your Additional functions or objects inside scope
        //
        //
        //


    }
);
