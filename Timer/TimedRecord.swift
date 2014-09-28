//
//  TimedRecord.swift
//  Timer
//
//  Created by Saga on 9/27/14.
//  Copyright (c) 2014 Charles. All rights reserved.
//

import Foundation
import UIKit

class TimedRecord {
    var tag: String!
    var date: NSDate!
    var seconds: Double!
    var parent: TimedItem!
    
    init(tag: String, date: NSDate, seconds: Double, parent: TimedItem) {
        self.tag = tag
        self.date = date
        self.seconds = seconds
        self.parent = parent
    }
}