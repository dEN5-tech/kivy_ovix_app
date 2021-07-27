Flickable{
  id: flick_panel
  anchors.fill: parent
 
  contentWidth: parent.width
  contentHeight: content_rect.height
  clip: true
 
  flickableDirection: Flickable.VerticalFlick
  BoundsBehavior: Flickable.StopAtBounds
 
  Column{            
      width: parent.width
      id: content_rect
  }
}

