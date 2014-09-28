//
//  ItemManager.swift
//  Timer
//
//  Created by Saga on 9/27/14.
//  Copyright (c) 2014 Charles. All rights reserved.
//

import Foundation
import UIKit

class ItemManager: NSObject {
    var items = [TimedItem]()
    
    override init() {
        
        items.append(TimedItem(tag: "Hello"))
        items.append(TimedItem(tag: "World World World"))
        
    }
}