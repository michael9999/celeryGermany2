var queryText = '';
sqlTest.setValue(queryText);

async function runBuild(){

const searchCriteria = searchvar.data;
//("1) test");
//("2) check table data : " + searchCriteria[0].kw);

let namesText = '';
//let queryText = '';

// loop through all the data in the table 
  // each row is a new criteria or condition for the search
const mappedArray = searchvar.data.map(item => {
  
  
  // Set the comparison type 

  var comparator = "";
  if (item.match == "not contains"){
    
    comparator = "NOT ILIKE";
    
  } else if (item.match == "contains"){
    
    comparator = "ILIKE";
    
  } else if (item.match == "is not") {
    
    comparator = "!=";
    
  } else if (item.match == "is"){
  
    comparator = "=";
    }
  else if (item.match == ">"){
  
    comparator = ">";
}
    else if (item.match == "<"){
  
    comparator = "<";
}
  
    // NO OPERATORS CHOSEN
  else{
    
    console.log("no comparison operators found");
    
  }
  
    // WHICH FIELDS?
  
  var fieldtoQuery = '';
  
  if (item.type == "job title") {
    // jobtitle
    fieldtoQuery = "job_title";
    
  } else if (item.type == "company") {
    
    fieldtoQuery = "company";
    
  } else if (item.type == "yrs exp") {
    
    fieldtoQuery = "years_exp";
    
  } else if (item.type == "location") {
    
    fieldtoQuery = "location";
    
  }
 
  // must be optimisedsearch field
  else {
    
    // this is full search
    fieldtoQuery = "optimisedsearch";
    
  }
  // end field to query
  

  // FIND out if this is the First argument, if not move to next

    if (item.level == "1st query") {

        console.log("1) 1st query");

        var first = "";
    
      // remove % for exact searches
        if(item.match == "is" || item.match == "is not") {
            
            queryText += `SELECT name, job_title, li_url, years_exp, company, date_contacted FROM candidates WHERE (LOWER(candidates.${fieldtoQuery}) ${comparator} '${item.kw}' `;
            
            //("exact1) - " + queryText)
            
        }
        else if (item.match == "contains" || item.match == "not contains"){

            queryText += `SELECT name, job_title, li_url, years_exp, company, date_contacted FROM candidates WHERE (LOWER(candidates.${fieldtoQuery}) ${comparator} '%${item.kw}%' `;
            

        }
        else if(item.match == ">") {
            
            queryText += `SELECT name, job_title, li_url, years_exp, company, date_contacted FROM candidates WHERE (candidates.${fieldtoQuery} ${comparator} '${item.kw}' `;
        
        //("> 1) - " + queryText);
            
        }
        
        else if(item.match == "<") {
            
            queryText += `SELECT name, job_title, li_url, years_exp, company, date_contacted FROM candidates WHERE (candidates.${fieldtoQuery} ${comparator} '${item.kw}' `;
        
        //("< 1) - " + queryText);
            
        }
    
  
  
    } 
  
    else { // NOT FIRST QUERY, check if "current" or "new"
    
        console.log("1) NOT 1st query");
    
        // remove % for exact searches
        if(item.match == "is" || item.match == "is not") {
            
            // check if a new level is required or not 
        
            if(item.level == 'new'){

                console.log("2) NOT 1st query");
                queryText += `) ${item.andor} (LOWER(candidates.${fieldtoQuery}) ${comparator} '${item.kw}'`
            
            //("new2) - " + queryText)

            }
            else { // this is not a new level
                
                console.log("3) NOT 1st query");
                queryText += ` ${item.andor} LOWER(candidates.${fieldtoQuery}) ${comparator} '${item.kw}'`
                
                //("else2) - " + queryText)
                
            }
            
            
            //queryText += ` ${item.andor} LOWER(candidates.${fieldtoQuery}) ${comparator} '${item.kw}'`
            
        }
        else if(item.match == "contains" || item.match == "not contains"){


            if(item.level == 'new'){

                console.log("2) NOT 1st query");
                queryText += `) ${item.andor} (LOWER(candidates.${fieldtoQuery}) ${comparator} '%${item.kw}%'`
            
            //("new2) - " + queryText)

            }
            else { // this is not a new level
                
                console.log("3) NOT 1st query");
                queryText += ` ${item.andor} LOWER(candidates.${fieldtoQuery}) ${comparator} '%${item.kw}%'`
                
                //("else2) - " + queryText)
                
            }


        }
        else if(item.match == ">") {


                if(item.level == 'new'){

                    console.log("4) NOT 1st query");
                    queryText += `) ${item.andor} (${fieldtoQuery} ${comparator} '${item.kw}'`
                    
                    //("new3) - " + queryText)
        
                    }
                else { // this is not a new level
                    
                    console.log("5) NOT 1st query");
                    queryText += ` ${item.andor} ${fieldtoQuery} ${comparator} '${item.kw}'`
                    
                    //("not new 3) - " + queryText)
                    
                    }   
                
            }
            
        else if(item.match == "<") {


                    if(item.level == 'new'){

                        console.log("6) NOT 1st query");
                        queryText += `) ${item.andor} (${fieldtoQuery} ${comparator} '${item.kw}'`
                        
                        //("< new 4) - " + queryText)
            
                        }else { // this is not a new level
                        
                            console.log("7) NOT 1st query");
                            queryText += ` ${item.andor} ${fieldtoQuery} ${comparator} '${item.kw}'`
                        //("< not new) - " + queryText)
                        
                        }    
                
                
                
            }
      
        else { /// NEED to CATER FOR YRS AND LOCATION HERE
            
            console.log("8) NOT 1st query");
        }  
      
    }

  //callback(queryText);
 return {
  queryText
 };
})
} // end of function

async function updateSqlValue(){
  
  //("updateSqlValue started: " + queryText);
  if(queryText && queryText != null){
    //("updateSqlValue) end of variable: " + queryText);
  queryText += ") LIMIT " + "2" + " OFFSET " + "10";
    //("updateSqlValue) FINAL QUERY " + queryText);
    sqlTest.setValue(queryText);
  }else {
    
    //("updateSqlValue) queryText null? " + queryText);
    
  }
  
  
}

const run = async () => {
  
  await runBuild();
  //("just after runBuild : " + queryText);
  await updateSqlValue();
  //("just after updateSqlValue");
  query7.trigger();
  
}

run();