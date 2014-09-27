//
//  ViewController.swift
//  Timer
//
//  Created by Charles on 14-9-27.
//  Copyright (c) 2014年 Charles. All rights reserved.
//

import UIKit

class ViewController:UIViewController {
    var screenSize:CGRect=UIScreen.mainScreen().bounds
    override func viewDidLoad() {
        super.viewDidLoad()
        let width=screenSize.width
        let height=screenSize.height
        let button:UIButton=UIButton(frame: CGRectMake(width/2-100,height/2-150, 200, 200))
        
        let timeLabel:UILabel=UILabel(frame: CGRectMake(width/2-100, height/2+150, 200, 100))
//        timeLabel.text=timeString
        timeLabel.textAlignment=NSTextAlignment.Center
        
        self.view.backgroundColor=UIColor.whiteColor()
        // Do any additional setup after loading the view, typically from a nib.
        button.backgroundColor=UIColor.yellowColor()
        view.addSubview(button)
        view.addSubview(timeLabel)
        
        button.addTarget(self, action: "change:", forControlEvents: UIControlEvents.TouchUpInside)
        
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func change(button:UIButton){
        button.backgroundColor=UIColor.blueColor()
    }
    
}

