//
//  SecondViewController.swift
//  Timer
//
//  Created by Charles on 14-9-27.
//  Copyright (c) 2014年 Charles. All rights reserved.
//
import Foundation
import UIKit

class SecondViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    @IBOutlet var recordTable: UITableView!
    
    var recordTimedItems = []
    var itemManager:ItemManager?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.view.backgroundColor=UIColor.whiteColor()
        self.recordTable.delegate = self
        self.recordTable.dataSource = self
        self.itemManager = ItemManager()
    }
    
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1;
    }
    
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return itemManager!.items.count;
    }
    
    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("ItemViewCell") as ItemViewCell // cast
        
        let timedItem = itemManager!.items[indexPath.row]
        cell.tagName!.text = timedItem.tag
        
        return cell
    }
    
    func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        
    }
}