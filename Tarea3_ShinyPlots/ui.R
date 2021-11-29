
library(shiny)

shinyUI(fluidPage(
    titlePanel("Tarea Shiny plots"),
    tabsetPanel(
        tabPanel("Interactive Plot 1", 
                 sidebarLayout(
                     sidebarPanel(
                         sliderInput("bins",
                                     "Number of bins:",
                                     min = 1,
                                     max = 50,
                                     value = 30),
                         selectInput("set_col", "Escoger color:",
                                     choices=c("aquamarine", "red", "blue", "darkgray", "gray", "green", "lightgray"), 
                                     selected = "aquamarine" ),
                         textInput("url_param", "Marcador:", value="")
                     ),
                     mainPanel(
                         plotOutput("distPlot", 
                                    hover="hist_mouse_hover", click="hist_click", dblclick="hist_dclick")
                     )
                 )
         ),
        tabPanel("Clicks plots", 
                 fluidRow(
                     column(6, plotOutput("plot_click_options", click="plotcars_click", brush="plotcars_brush")
                     ),
                     column(6, DT::dataTableOutput("mtcars_tbl") )
                 )
        )
        
        )
))
