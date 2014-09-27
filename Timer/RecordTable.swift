//
//  RecordTable.swift
//  Timer
//
//  Created by Charles on 14-9-27.
//  Copyright (c) 2014年 Charles. All rights reserved.
//

import UIKit

class RecordTable: UITableView,UITableViewDelegate,UITableViewDataSource {
    
    var recordTable:RecordTable?
    var recordData=["1","2","3","4","5"]
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return recordData.count
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("id") as UITableViewCell
        cell.textLabel?.text="Test"
        return cell
    }
    
}
