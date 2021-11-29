
library(shiny)

shinyServer(function(input, output, session) {
    
    # observa todos los inputs dentro de las llaves para detectar cambios.
    # A continuacion se le da capacidad de recibir y leer parametros desde un query parameter.
    observe({
        query <- parseQueryString(session$clientData$url_search)
        bins <- query[["bins"]]
        bar_col <- query[["color"]]
        if (!is.null(bins)) {
            updateSliderInput(session, "bins", value=as.numeric(bins))
        }
        if (!is.null(bar_col)) {
            updateSelectInput(session, "set_col", selected=bar_col)
        }
    })
    
    observe({
        bins <- input$bins
        color <- input$set_col
        
        host_name <- session$clientData$url_hostname
        protocol <- session$clientData$url_protocol
        port <- session$clientData$url_port
        query <- paste("?", "bins=", bins, "&color=", color, sep="") #session$clientData$url_search
        
        url <- paste(protocol, "//", host_name, ":", port, "/", query, sep="")
        updateTextInput(session, "url_param", value=url)
    })

    output$distPlot <- renderPlot({
        x <- faithful[,2]
        hist(x, breaks=input$bins, col=input$set_col, border="white")
    })

    observe({
        # Tarea 1: 1) On hover cambie el color a gris
        if (!is.null(input$hist_mouse_hover) && input$hist_mouse_hover$x > 0) {
            updateSelectInput(session, "set_col", selected="gray")
        }
        # Tarea 1: 2) On click cambie el color a verde
        if (!is.null(input$hist_click) && input$hist_click$x > 0) {
            updateSelectInput(session, "set_col", selected="green")
        }
        # Tarea 1: 3) On doble click quite el color. Quitar el color, es poner col a su valor default, es decir, "lightgray"
        if (!is.null(input$hist_dclick) && input$hist_dclick$x > 0) {
            updateSelectInput(session, "set_col", selected="lightgray")
        }
    })
    
    
    
    output$plot_click_options <- renderPlot({
        plot(mtcars$wt, mtcars$mpg, xlab="wt", ylab="Miles per galon")
    })
    
    # Para que la tabla muestre el valor de donde se hizo click en la grafica.  
    output$mtcars_tbl <- DT::renderDataTable({
        print(paste("BRUSH: ", is.null(input$plotcars_brush)))
        print(paste("CLICK: ", is.null(input$plotcars_click)))
        if (is.null(input$plotcars_brush) && !is.null(input$plotcars_click)) {
            # 5. On click mostramos la información del punto en una tabla
            df <- nearPoints(mtcars, input$plotcars_click, xvar="wt", yvar="mpg")
            df
        } else if (!is.null(input$plotcars_brush) && !is.null(input$plotcars_click)) {
            # 6. On brush mostramos todos los puntos en el rectángulo
            df <- brushedPoints(mtcars, input$plotcars_brush, xvar="wt", yvar="mpg")
            df
        }
    })
    
    
    
    # https://jokergoo.github.io/2021/02/20/differentiate-brush-and-click-event-in-shiny/
})
