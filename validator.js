$.validator.prototype.focusInvalid= function() {
        			if ( this.settings.focusInvalid ) {
        				try {
        					var _element = $(this.findLastActive() || this.errorList.length && this.errorList[0].element || [])
        					.filter(":visible");
        					if(_element&&_element.context){
        						var tab = $(_element.context).closest(".tab-pane");
        						if(tab.hasClass("active")){
        							//ignore
        						}else{
        							$("a[href='#"+tab[0].id+"']")[0].click();
        						}
        					}
        					
        					$(this.findLastActive() || this.errorList.length && this.errorList[0].element || [])
        					.filter(":visible")
        					.focus()
        					// manually trigger focusin event; without it, focusin handler isn't called, findLastActive won't have anything to find
        					.trigger("focusin");
        				} catch(e) {
        					// ignore IE throwing errors when focusing hidden elements
        				}
        			}
        		};
