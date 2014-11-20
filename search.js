<style>
	.lbl{
		display: inline;
		padding: .2em .6em .3em;
		font-size: 100%;
		line-height: 1;
		text-align: center;
		white-space: nowrap;
		vertical-align: baseline;
	}
	.lbluncheck{
		cursor: pointer;
	}
	.lblchecked{
		background-color: #5bc0de;
		display: inline;
		padding: .2em .6em .3em;
		font-size: 100%;
		font-weight: 700;
		line-height: 1;
		color: #fff;
		text-align: center;
		white-space: nowrap;
		vertical-align: baseline;
		border-radius: .25em;
	}
	
	.search_conditions b{
		font-size: 14px;;
	}
</style>
					
<form id="search_todo_conditions" class="search_conditions">
		
	<div class="col-md-12 form-group lbl-group" >
		<b class="">流程名称:</b>
		
		<label class="lbl lblchecked" >全部
			<input type="radio" class=" hidden"
			value="" checked="checked" name="processType" />
		</label>
		
		<label class="lbl lbluncheck" >易贷集中审批流程
			<input type="radio" class="hidden"
			value="1003" name="processType" />
		</label>
		
		<label class="lbl lbluncheck">微贷集中审批流程
			<input type="radio" class="hidden"
			value="1004" name="processType" />
		</label>
	</div>
	
	<div class="col-md-12 form-group lbl-group" >
		<b class="">流程状态:</b>
		
		<label class="lbl lblchecked" >全部
			<input type="radio" class=" hidden"
			value="" checked="checked" name="processStatus" />
		</label>
		
		<label class="lbl lbluncheck" >待处理
			<input type="radio" class="hidden"
			value="80" name="processStatus" />
		</label>
		
		<label class="lbl lbluncheck">处理中
			<input type="radio" class="hidden"
			value="81" name="processStatus" />
		</label>
		
		<label class="lbl lbluncheck">处理完成
			<input type="radio" class="hidden"
			value="82" name="processStatus" />
		</label>
	</div>
	
	<div class="col-md-2 form-group">
    	<b class="">任务主题:</b>
	  	<input name="taskSubject" type="text" class="input-small">
	</div>
	
	<div class="col-md-2 form-group">
    	<b class="">提交时间:开始</b>
	  	<input name="submitTimeStart" id="submitTimeStart"
			  	 type="text" class="input-small"/>
	</div>
	
	<div class="col-md-2 form-group">
    	<b class="">提交时间:结束</b>
	  	<input name="submitTimeEnd" id="submitTimeEnd"
	  	 type="text" class="input-small"/>
	</div>
	
	<div class="col-md-2">
		<button id="do_search_condition" type="button"
		class="btn btn-sm btn-purple">
		<i class="ace-icon fa fa-search"></i> 查询</button>
	</div>
	
</form>	
initSearchConditions : function(){
	var viewSelf = this;
	$(document).on("click","#do_search_condition",function(){
		viewSelf.toDoTable.refreshParamCache();
		viewSelf.toDoTable.fnPageChange(0);
	});
	$("#search_todo_conditions").on("click",".lbl",function(e){
		$(this).closest(".lbl-group").find(".lbl").addClass("lbluncheck")
		.removeClass("lblchecked");
		$(this).removeClass("lbluncheck")
		.addClass("lblchecked").find("input[type='radio']")[0].click();
		viewSelf.toDoTable.refreshParamCache();
		viewSelf.toDoTable.fnPageChange(0);
	});
},
var toDoTable = $("#tbl_todo").dataTable({
				bLengthChange: false,
				bServerSide: true,
				bFilter: false,
		    	sAjaxSource: $$ctx + "?/search",
		    	fnServerParams: function (aoData) {
		    		if(!this.serverParamCache){
                		this.refreshParamCache = function(){
                			this.serverParamCache = $("#search_todo_conditions").serializeArray();
                			
                        };
                        
                        this.refreshParamCache();
                	}
		    		
                	$(this.serverParamCache).each(function(i,d){
                		aoData.push(d);
                	});
				},
