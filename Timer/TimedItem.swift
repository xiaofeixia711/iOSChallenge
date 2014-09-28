//
//  TimedItem.swift
//  Timer
//
//  Created by Saga on 9/27/14.
//  Copyright (c) 2014 Charles. All rights reserved.
//

import Foundation
import UIKit

class TimedItem {
    var tag: String!
    var averageTime: Double!
    var estimatedTime: Double!
    var records: [TimedRecord]!
    
    init(tag: String) {
        self.tag = tag
        self.averageTime = 0
        self.estimatedTime = 0
        self.records = []
    }
    
    
}